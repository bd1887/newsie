from newsie.models import Article
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from utils.dummy_fun import dummy_fun

# World Max s_score: .73 - .133
# Sports Max s_score: .6 - .166

def calculate_eps():
    articles = Article.objects.filter(category__exact='World')
    #Creates a list of the pre-processed Article tokens
    texts = [art.tokens for art in articles]

    tfidf = TfidfVectorizer(
    use_idf=True,
    tokenizer=dummy_fun, #No need to pre-process,
    preprocessor=dummy_fun) # since it was done while webscraping
    
    tfidf_matrix = tfidf.fit_transform(texts)
    tfidf_matrix = tfidf_matrix.todense()

    # nbrs = NearestNeighbors(n_neighbors=3, metric='cosine').fit(tfidf_matrix)
    # distances, indices = nbrs.kneighbors(tfidf_matrix)
    # distances = distances[:,2]
    # distances = np.sort(distances, axis=0)

    # print(len(distances))

    # # nbrs = NearestNeighbors(n_neighbors=2, metric='cosine').fit(tfidf_matrix)
    # # distances, indices = nbrs.kneighbors(tfidf_matrix)
    # # distances = np.sort(distances, axis=0)
    # # distances = distances[:,1]
    # plt.plot(distances)
    # plt.show()

    from sklearn import metrics

    eps = .05
    s_scores = []
    eps_values = []

    while eps <= 1:
        dbscan = DBSCAN(eps=eps, min_samples=1, metric='cosine')
        model = dbscan.fit(tfidf_matrix)
        labels = model.labels_
        s_score = metrics.silhouette_score(tfidf_matrix, labels, metric="cosine")
        s_scores.append(s_score)
        eps_values.append(eps)
        eps = eps + 0.05

    plt.plot(eps_values, s_scores)
    plt.ylabel('Silhouette')
    plt.xlabel('Epsilon')
    plt.show()


# clusters = dbscan.fit_predict(tfidf_matrix)
#         model = dbscan.fit(tfidf_matrix)
        
# n_clusters = len(set(labels)) - (1 if -1 in labels else 0)


    # #The highest generated topic number, for iterating
    # num_topics = max(clusters) + 1

    # sorted_articles = []

    # # create list for each topic
    # for i in range(num_topics):
    #     sorted_articles.append([])

    # #Puts articles in lists according to their topic number
    # for idx, art in enumerate(articles):
    #     if clusters[idx] > -1: #Article has a cluster
    #         topic_num = clusters[idx] #Get cluster number
    #         sorted_articles[topic_num].append(art) #Append Article to its cluster list
    #     else: #Article has no cluster
    #         sorted_articles.append([articles[idx]]) #Put Article in a list by itself

    # sorted_articles.sort(key=len, reverse=True) #Sort with largest clusters first

    # for cluster in sorted_articles:
    #     if len(cluster) >= 5:
    #         print(cluster)
    #         print('------------------------------------')