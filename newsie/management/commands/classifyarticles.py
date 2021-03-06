from django.core.management.base import BaseCommand
from newsie.scripts.classify_articles import classify_articles

class Command(BaseCommand):
    help = 'Classifies articles with no category classification'

    def handle(self, *args, **kwargs):
        self.stdout.write("Classifying articles... ")
        classify_articles()
        self.stdout.write("Done!")