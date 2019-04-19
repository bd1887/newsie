from django.core.management.base import BaseCommand
from newsie.scripts.classify_articles import classify_articles

class Command(BaseCommand):
    help = 'Trains category classifier on labeled articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Training category model... ")
        self.train_classifier()
        self.stdout.write("Done!")

    
