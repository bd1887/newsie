from newsie.models import Article
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import DBSCAN
from utils.dummy_fun import dummy_fun
from sklearn import metrics
from newsie.publications.get_articles import categories

def average_silhouette():

    top_eps_values = []
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
        top_s_score = 0
        top_eps_value = 0

        while eps <= 1:
            dbscan = DBSCAN(eps=eps, min_samples=2, metric='cosine')
            model = dbscan.fit(tfidf_matrix)
            labels = model.labels_
            if np.unique(labels).size >= 2:
                s_score = metrics.silhouette_score(tfidf_matrix, labels, metric="cosine")
                if s_score > top_s_score:
                    top_s_score = round(s_score, 3)
                    top_eps_value = eps
            eps = round(eps + 0.05, 2)

        print(f"Category: {category} | Top S_Score: {top_s_score} | Eps Value: {top_eps_value}")
        top_eps_values.append(top_eps_value)
        top_s_score = 0
        top_eps_value = 0

    average_top_eps_value = round(np.mean(top_eps_values), 3)
    print(top_eps_values)
    print(f"Average Top Eps Value: {average_top_eps_value}")

