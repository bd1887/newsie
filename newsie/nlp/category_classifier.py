from newsie.models import Article
from utils.dummy_fun import dummy_fun
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from joblib import dump, load
from sklearn.pipeline import make_pipeline


def train(articles):
    news_df = pd.DataFrame.from_records([art.to_dict() for art in articles])
    X_train, X_test, y_train, y_test = train_test_split(
        news_df['text'], 
        news_df['category'], 
        random_state = 1
    )

    count_vector = CountVectorizer(
        analyzer='word',
        tokenizer=dummy_fun,
        preprocessor=dummy_fun,
        token_pattern=None
        )
    training_data = count_vector.fit_transform(X_train)
    testing_data = count_vector.transform(X_test)

    model = LogisticRegression()

    pipe = make_pipeline(count_vector, model)

    model.fit(training_data, y_train)
    predictions = model.predict(testing_data)
    print("Accuracy score: ", accuracy_score(y_test, predictions))
    print("Recall score: ", recall_score(y_test, predictions, average = 'weighted'))
    print("Precision score: ", precision_score(y_test, predictions, average = 'weighted'))
    print("F1 score: ", f1_score(y_test, predictions, average = 'weighted'))

    dump(pipe, 'model.joblib')

    return news_df

def classify(article):
    pipe = load('model.joblib')
    tokens = article.tokens
    category = pipe.predict([tokens])
    probability = pipe.predict_proba([tokens])
    probability = max(probability[0])
    article.category = category[0]
    print(f"Prediction: {category[0]} {probability} | {article.url}")
    
    classification = category[0] if probability > .98 else ''

    return classification
