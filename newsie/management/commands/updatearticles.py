from django.core.management.base import BaseCommand
from newsie.scripts.update_articles import update_articles

class Command(BaseCommand):
    help = 'Runs webscraper to find new articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Getting todays' news articles. This may take several minutes...")
        update_articles()
        self.stdout.write("Done!")
