from django.core.management.base import BaseCommand
from newsie.scripts.classify_articles import classify_articles

class Command(BaseCommand):
    help = 'Classifies unlabeled articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Classifying category model... ")
        classify_articles()
        self.stdout.write("Done!")