from newsie.models import Article
from newsie.publications.get_articles import categories
from newsie.nlp.tokenize import tokenize

def retokenize():
    for category in categories():
        query_set = Article.objects.filter(category__exact=category)

        query_set = tokenize(query_set)

        for article in query_set:
            article.save()