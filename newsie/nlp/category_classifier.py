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
    pipe = load('model.joblib')
    df = pd.DataFrame.from_records([article.to_dict()])
    category = pipe.predict(df)[0]
    probability = pipe.predict_proba(df)
    probability = max(probability[0])
    article.category = category[0]
    # print(f"Prediction: {category[0]} {probability} | {article.url}")
    
    print(f'{category} | {probability}')
    print(article.title)
    print('--------')
    print(' ')
    classification = category if probability > .93 else ''

    return classification


class DataFrameColumnExtracter(TransformerMixin):

    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[self.column]

def train(articles):
    clf = svm.SVC(kernel='linear', probability=True)
    cvec = CountVectorizer(
        analyzer='word',
        tokenizer=dummy_fun,
        preprocessor=dummy_fun,
        token_pattern=None
        )

    tfidf = TfidfVectorizer(
        analyzer='word',
        tokenizer=dummy_fun,
        preprocessor=dummy_fun,
        token_pattern=None
        )


    news_df = pd.DataFrame.from_records([art.to_dict() for art in articles])
    
    X = news_df.drop('category', 1)
    Y = news_df['category']

    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        Y, 
        random_state = 42,
        test_size=0.33
    )

    pipe = Pipeline([
        ('features', FeatureUnion([
                ('url_tokens', Pipeline([
                    ('selector', DataFrameColumnExtracter('url_tokens')),
                    ('vec', cvec)
                ])),
                ('text_features', Pipeline([
                    ('selector', DataFrameColumnExtracter('tokens')),
                    ('vec', tfidf)
                ]))
            ])),
        ('clf', OneVsRestClassifier(clf))
    ])

    pipe.fit(X_train, y_train)
    print(pipe.score(X_test, y_test))
    dump(pipe, 'model.joblib')

    return news_df