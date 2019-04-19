from django.core.management.base import BaseCommand
from newsie.scripts.classify_articles import classify_articles
from newsie.scripts.clean_clusters import clean_clusters
from newsie.scripts.find_top_stories import find_top_stories
from newsie.scripts.merge_clusters import merge_clusters
from newsie.scripts.train_classifier import train_classifier
from newsie.scripts.update_articles import update_articles

class Command(BaseCommand):
    help = 'Runs all necessary scheduled tasks.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Getting todays' news articles. This may take several minutes...")
        update_articles()

        self.stdout.write("Training topic classifier...")
        train_classifier()

        self.stdout.write("Classifying unlabeled articles...")
        classify_articles()

        self.stdout.write("Merging article topics...")
        merge_clusters()

        self.stdout.write("Finding today's top stories...")
        find_top_stories()

        self.stdout.write("Cleaning clusters...")
        clean_clusters()

        self.stdout.write("Done!")