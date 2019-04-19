from newsie.models import Article
from newsie.nlp.category_classifier import train

def train_classifier():
    articles = Article.objects.all().exclude(labeled__exact=False).exclude(category__exact='')
    train(articles)