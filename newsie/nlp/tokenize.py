from django.core.management.base import BaseCommand
from django.db.models import Max
from newsie.models import Article
from newsie.publications import get_articles
from newsie.nlp.dbscan import dbscan
from newsie.publications import get_articles
import datetime
from django.utils import timezone
from gensim.parsing.preprocessing import remove_stopwords
from gensim.models import Phrases
from gensim.models.phrases import Phraser
import nltk, re, string, collections
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

from gensim.utils import lemmatize
from gensim.parsing.preprocessing import remove_stopwords
from gensim.models import Phrases

def tokenize(articles):

    # Punctuation to be removed
    punct = string.punctuation + "'“”'‘’–"
    regex = "[" + re.sub("\.","",punct) + "]"

    for article in articles:
        tokens = re.sub(regex, "", article.get_text()) #strip punctuation
        tokens = tokens.lower()
        tokens = remove_stopwords(tokens) #remove common words such as articles and prepositions
        tokens = lemmatize(tokens) #finds the lemma, a kind of root form of the word
        lemmatized_out = [token.decode('utf-8').split('/')[0] for token in tokens] #strip part-of-speech tag
        article.tokens = lemmatized_out

    # Create a list of lists of article tokens
    documents = [article.tokens for article in articles]

    vocabulary = []
    for document in documents:
        for token in document:
            if token not in vocabulary:
                vocabulary.append(token)

    print(f"Vocabulary Length: {len(vocabulary)}")

    # Generate ngrams (collocative phrases) from the tokens
    bigram = Phrases(documents, min_count=3, threshold=15, delimiter=b'_') #set threshold for bigrams somewhat low
    trigram = Phrases(bigram[documents], min_count=4, threshold=40, delimiter=b'_') #set threshold for trigrams somewhat high to avoid spurrious phrases

    document_tokens = []

    # Applies the ngram models to each document (the article tokens)
    for doc in documents:
        bigrams = [b for b in bigram[doc]]
        document_tokens.append([t for t in trigram[bigram[doc]]])

    # Assigns the generated tokens to the tokens attribute of each Article object
    for idx, article in enumerate(articles):
        articles[idx].tokens = document_tokens[idx]
    
    return articles