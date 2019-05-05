from newsie.models import Article
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from utils.dummy_fun import dummy_fun
from sklearn import metrics
from newsie.publications.get_articles import categories

# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'brown']


def plot_silhouette():
    for index, category in enumerate(categories()):
        articles = Article.objects.filter(category__exact=category)

        #Creates a list of the pre-processed Article tokens
        texts = [art.tokens for art in articles]

        tfidf = TfidfVectorizer(
        use_idf=True,
        tokenizer=dummy_fun, #No need to pre-process,
        preprocessor=dummy_fun) # since it was done while webscraping
        
        tfidf_matrix = tfidf.fit_transform(texts)
        # tfidf_matrix = tfidf_matrix.todense()

        eps = .05
        top_eps_values = []
        s_scores = []
        eps_values = []
        top_s_score = 0
        top_eps_value = 0

        while eps <= 1:
            dbscan = DBSCAN(eps=eps, min_samples=2, metric='cosine')
            model = dbscan.fit(tfidf_matrix)
            labels = model.labels_
            if np.unique(labels).size >= 2:
                s_score = metrics.silhouette_score(tfidf_matrix, labels, metric="cosine")
                s_scores.append(s_score)
                if s_score > top_s_score:
                    top_s_score = s_score
                    top_eps_value = eps
                eps_values.append(eps)
            eps = eps + 0.05

        top_eps_values.append(top_eps_value)
        top_s_score = 0
        top_eps_value = 0
        plt.plot(eps_values, s_scores, label=category)

    plt.ylabel('Silhouette Score')
    plt.xlabel('Epsilon Value')
    plt.legend(loc='upper left')
    average_top_eps_value = np.mean(top_eps_values)
    print(f"Average Top Silhouette Score: {average_top_eps_value}")
    plt.show()

# def plot_silhouette():
#     articles = Article.objects.filter(category__exact='World')
#     #Creates a list of the pre-processed Article tokens
#     texts = [art.tokens for art in articles]

#     tfidf = TfidfVectorizer(
#     use_idf=True,
#     tokenizer=dummy_fun, #No need to pre-process,
#     preprocessor=dummy_fun) # since it was done while webscraping
    
#     tfidf_matrix = tfidf.fit_transform(texts)
#     tfidf_matrix = tfidf_matrix.todense()

#     from sklearn import metrics

#     eps = .05
#     s_scores = []
#     eps_values = []

#     while eps <= 1:
#         dbscan = DBSCAN(eps=eps, min_samples=1, metric='cosine')
#         model = dbscan.fit(tfidf_matrix)
#         labels = model.labels_
#         s_score = metrics.silhouette_score(tfidf_matrix, labels, metric="cosine")
#         s_scores.append(s_score)
#         eps_values.append(eps)
#         eps = eps + 0.05

#     plt.plot(eps_values, s_scores)
#     plt.ylabel('Silhouette')
#     plt.xlabel('Epsilon')
#     plt.show()
