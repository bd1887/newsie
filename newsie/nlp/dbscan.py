import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN

def dbscan(articles):

    if len(articles) == 0:
        return []

    texts = [art.get_text() for art in articles]
    texts = [art.lower() for art in texts]

    stopset = set(stopwords.words('english'))
    # stopset.update(['just', 'some', 'examples'])

    tfidf = TfidfVectorizer(stop_words=stopset, use_idf=True, ngram_range=(1, 3))
    tfidf_matrix = tfidf.fit_transform(texts)


    dbscan = DBSCAN(eps=0.8, min_samples=2, metric='cosine', algorithm='auto')

    labels = dbscan.fit_predict(tfidf_matrix)
    num_topics = max(labels) + 1
    print("Number of topics: ", num_topics)

    sorted_articles = []

    for i in range(num_topics):
        sorted_articles.append([])

    for idx, art in enumerate(articles):
        if labels[idx] > -1:
            topic_num = labels[idx]
            sorted_articles[topic_num].append(art)
        else:
            sorted_articles.append([articles[idx]])

    return sorted_articles
