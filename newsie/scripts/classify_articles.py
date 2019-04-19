from newsie.nlp.category_classifier import classify
from newsie.models import Article

def classify_articles():
        articles = Article.objects.all().filter(category__exact='')

        for art in articles:
            category = classify(art)
            art.category = category
            art.save()