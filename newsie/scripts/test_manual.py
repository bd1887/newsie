from newsie.models import Article
from newsie.nlp.category_classifier import classify

def test_manual():
    articles = Article.objects.all().exclude(labeled__exact=True).exclude(manual_label__exact='')
    total = len(articles)
    matches = 0
    for article in articles:
        classification = classify(article)
        if classification == article.manual_label:
            matches += 1

    print(f"Percent matches: {matches / total} out of {len(articles)} manually labeled articles")