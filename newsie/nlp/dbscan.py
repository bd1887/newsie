from utils.dummy_fun import dummy_fun
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import DBSCAN

def dbscan(articles):

    #Creates a list of the pre-processed Article tokens
    texts = [art.tokens for art in articles]

    tfidf = TfidfVectorizer(
    use_idf=True,
    tokenizer=dummy_fun, #No need to pre-process,
    preprocessor=dummy_fun) # since it was done while webscraping
    
    tfidf_matrix = tfidf.fit_transform(texts)

    #eps was chosen somewhat arbitrarily; more testing required
    dbscan = DBSCAN(eps=0.75, min_samples=2, metric='cosine')

    #Generates a list of cluster numbers (or -1 for noise)
    #whose indexes correspond to the indexes of the Articles list
    clusters = dbscan.fit_predict(tfidf_matrix)

    #The highest generated topic number, for iterating
    num_topics = max(clusters) + 1

    sorted_articles = []

    # create list for each topic
    for i in range(num_topics):
        sorted_articles.append([])

    #Puts articles in lists according to their topic number
    for idx, art in enumerate(articles):
        if clusters[idx] > -1: #Article has a cluster
            topic_num = clusters[idx] #Get cluster number
            sorted_articles[topic_num].append(art) #Append Article to its cluster list
        else: #Article has no cluster
            sorted_articles.append([articles[idx]]) #Put Article in a list by itself

    sorted_articles.sort(key=len, reverse=True) #Sort with largest clusters first

    return sorted_articles