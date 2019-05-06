from django.core.management.base import BaseCommand
from newsie.scripts.train_classifier import train_classifier

class Command(BaseCommand):
    help = 'Trains category classifier on labeled articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Training classifier... ")
        train_classifier()
        self.stdout.write("Done!")

    
