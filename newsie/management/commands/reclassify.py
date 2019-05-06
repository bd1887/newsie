from django.core.management.base import BaseCommand
from newsie.scripts.reclassify import reclassify

class Command(BaseCommand):
    help = 'Re-classifies all unlabeled articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Classifying articles... ")
        reclassify()
        self.stdout.write("Done!")