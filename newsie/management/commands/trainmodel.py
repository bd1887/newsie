from django.core.management.base import BaseCommand
from newsie.models import Article
from newsie.nlp.category_classifier import train

class Command(BaseCommand):
    help = 'Runs webscraper'

    def handle(self, *args, **kwargs):
        self.stdout.write("Training category model... ")
        self.train_classifier()
        self.stdout.write("Done!")

    def train_classifier(self):
        articles = Article.objects.all().exclude(labeled__exact=False).exclude(category__exact='')
        train(articles)
