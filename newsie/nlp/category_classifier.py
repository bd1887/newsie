from newsie.models import Article
from utils.dummy_fun import dummy_fun
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from joblib import dump, load
from sklearn.pipeline import Pipeline, TransformerMixin, FeatureUnion
from sklearn.multiclass import OneVsRestClassifier

def classify(article):
    #load the trained classifier
    pipe = load('model.joblib')

    #convert the article to a dictionary then DataFrame
    df = pd.DataFrame.from_records([article.to_dict()]) 

    #0th index will be the category with the highest probability
    category = pipe.predict(df)[0]

    #Find the probability of the most likely category
    probability = pipe.predict_proba(df)
    probability = max(probability[0])

    #If probability is greater than the threshold, return a category
    classification = category if probability >= .93 else ''

    if probability >= .93:
        print(f"Classified Article: '{article.title}' \n Class: {classification} -- {probability} \n")

    return classification


class DataFrameColumnExtracter(TransformerMixin):

    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.column]

def train(articles):
    #Support Vector Machine:
    clf = svm.SVC(
        kernel='linear', #our data is linearly separable
        probability=True #we need probability to be calculated
        )
    # cvec = CountVectorizer(
    #     tokenizer=dummy_fun, #function that does nothing
    #     preprocessor=dummy_fun #since we already preprocessed
    #     )
    tfidf = TfidfVectorizer(tokenizer=dummy_fun, preprocessor=dummy_fun)

    #Converts Article objects to dictionaries for use in DataFrames
    news_df = pd.DataFrame.from_records([art.to_dict() for art in articles])
    
    #Creates two columns (features):
    #1 'tokens', the tokens from the article's body
    #2 'url_tokens', the tokens from the article's url
    X = news_df.drop('category', 1)

    #Creates one column with the categories (labels)
    Y = news_df['category']

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        Y, 
        random_state = 42, #pseudo-random number generator for consistent results
        test_size=0.33 #splits 33% of data into test group
    )

    # # Logistic Regression:
    #     # Accuracy on train_test_split: .95
    #     # Accuracy on manually labeled data: .61

    # # SVM:
    #     # Accuracy on train_test_split data: .96
    #     # Accuracy on manually labeled data: .60
    # pipe = Pipeline([
    #     ('features', FeatureUnion([
    #             ('url_tokens', Pipeline([
    #                 #DataFrameColumnExtracter is a custom class
    #                 #used for selecting the column with the correct feature
    #                 ('selector', DataFrameColumnExtracter('url_tokens')),
    #                 ('vec', cvec) # Count vectorizer
    #             ])),
    #             ('article_tokens', Pipeline([
    #                 ('selector', DataFrameColumnExtracter('tokens')),
    #                 ('vec', tfidf) # Tf-idf vectorizer
    #             ]))
    #         ])),
    #     ('clf', OneVsRestClassifier(clf))
    # ])

    # Logistic Regression:
        # #Accuracy on train_test_split data: .95
        # #Accuracy on manually labeled data: .60

    # SVM:
        # #Accuracy on train_test_split data: .89
        # #Accuracy on manually labeled data: .73
    pipe = Pipeline([
        ('article_tokens', Pipeline([
                    ('selector', DataFrameColumnExtracter('tokens')),
                    ('vec', tfidf), # Tf-idf vectorizer
                    ('clf', clf)    # SVM Classifier
                ]))
    ])

    pipe.fit(X_train, y_train) #Trains the classifier
    dump(pipe, 'model.joblib') #Saves the classifier as a .joblib file

    print(pipe.score(X_test, y_test))
    return news_df