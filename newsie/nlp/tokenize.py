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

def tokenize(articles):

    punct = string.punctuation + "'“”'‘’–"
    regex = "[" + re.sub("\.","",punct) + "]"

    for article in articles:
        tokens = re.sub(regex, "", article.get_text())
        tokens = tokens.lower()
        tokens = remove_stopwords(tokens)
        tokens = lemmatize(tokens)
        lemmatized_out = [token.decode('utf-8').split('/')[0] for token in tokens]
        article.tokens = lemmatized_out

    documents = [article.tokens for article in articles]

    bigram = Phrases(documents, min_count=2, threshold=15, delimiter=b'_')
    trigram = Phrases(bigram[documents], min_count=2, threshold=25, delimiter=b'_')

    document_tokens = []

    for doc in documents:
        # bigrams_ = [b for b in bigram[doc]]
        document_tokens.append([t for t in trigram[bigram[doc]]])

    for idx, article in enumerate(articles):
        articles[idx].tokens = document_tokens[idx]
    
    return articles