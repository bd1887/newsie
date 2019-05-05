from newsie.models import Article
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.dummy_fun import dummy_fun
from newsie.publications.get_articles import categories

# colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'brown']

def plot_nn():
    for index, category in enumerate(categories()):
        articles = Article.objects.filter(category__exact=category)
        texts = [art.tokens for art in articles]

        tfidf = TfidfVectorizer(
        use_idf=True,
        tokenizer=dummy_fun, #No need to pre-process,
        preprocessor=dummy_fun) # since it was done while webscraping
        
        tfidf_matrix = tfidf.fit_transform(texts)
        tfidf_matrix = tfidf_matrix.todense()

        nbrs = NearestNeighbors(n_neighbors=3, metric='cosine').fit(tfidf_matrix)
        distances, indices = nbrs.kneighbors(tfidf_matrix)
        distances = distances[:,2]
        distances = np.sort(distances, axis=0)

        plt.plot(distances, label=category)

    plt.legend(loc='lower right')
    plt.ylabel('Nearest Neighbor Cosine Similarity')
    plt.xlabel('Document Number (Sorted by Nearest Neighbor Proximity)')
    plt.show()
