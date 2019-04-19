from django.core.management.base import BaseCommand
from newsie.scripts.clean_clusters import clean_clusters

class Command(BaseCommand):
    help = 'Clear empty and unimportant ArticleClusters'

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing unimportant stories...")
        clean_clusters()
        self.stdout.write("Done!")
