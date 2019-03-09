from utils.dummy_fun import dummy_fun
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cluster import DBSCAN

def dbscan(articles):

    if len(articles) == 0:
        return []

    # get text from Article object, to lowercase
    texts = [art.tokens for art in articles]

    tfidf = TfidfVectorizer(
    use_idf=True,
    analyzer='word',
    tokenizer=dummy_fun, #No need to preprocess,
    preprocessor=dummy_fun, # since it was done while webscraping
    token_pattern=None)  
    
    tfidf_matrix = tfidf.fit_transform(texts)

    dbscan = DBSCAN(eps=0.75, min_samples=2, metric='cosine', algorithm='auto')

    labels = dbscan.fit_predict(tfidf_matrix)
    num_topics = max(labels) + 1

    print("*****************************")
    print(f"Num topics: {num_topics}")
    print(f"Total artices: {len(articles)}")

    sorted_articles = []

    # create list for each topic
    for i in range(num_topics):
        sorted_articles.append([])

    for idx, art in enumerate(articles):
        if labels[idx] > -1: #Article has a cluster
            topic_num = labels[idx] #Get cluster number
            sorted_articles[topic_num].append(art) #Append Article to its cluster list
        else: #Article has no cluster
            sorted_articles.append([articles[idx]]) #Put Article in a list by itself

    sorted_articles.sort(key=len, reverse=True) #Sort with largest clusters first

    return sorted_articles