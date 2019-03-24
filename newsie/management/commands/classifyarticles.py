from django.core.management.base import BaseCommand
from newsie.models import Article
from newsie.nlp.category_classifier import classify

class Command(BaseCommand):
    help = 'Runs webscraper'

    def handle(self, *args, **kwargs):
        self.stdout.write("Classifying category model... ")
        self.classify_articles()
        self.stdout.write("Done!")

    def classify_articles(self):
        articles = Article.objects.all().filter(category__exact='')

        for art in articles:
            category = classify(art)
            art.category = category
            art.save()
