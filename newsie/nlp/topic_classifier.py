from newsie.models import Article
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
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
    
    # print("Training dataset: ", X_train.shape[0])
    # print("Test dataset: ", X_test.shape[0])

    count_vector = CountVectorizer(stop_words = 'english')
    training_data = count_vector.fit_transform(X_train)
    testing_data = count_vector.transform(X_test)

    model = LogisticRegression()

    pipe = make_pipeline(count_vector, model)

    model.fit(training_data, y_train)
    predictions = model.predict(testing_data)
    print(predictions)
    print("Accuracy score: ", accuracy_score(y_test, predictions))
    print("Recall score: ", recall_score(y_test, predictions, average = 'weighted'))
    print("Precision score: ", precision_score(y_test, predictions, average = 'weighted'))
    print("F1 score: ", f1_score(y_test, predictions, average = 'weighted'))

    dump(pipe, 'model.joblib')

    return news_df

def classify(article):
    pipe = load('model.joblib')
    category = pipe.predict([article.get_text()])
    probability = pipe.predict_proba([article.get_text()])
    probability = max(probability[0])
    article.category = category[0]
    html_string = "<h2>" + article.title + "</h2>"
    html_string += "<h3>" + category[0] + " | " + str(probability) + "</br>"

    return html_string
    # model.predict()