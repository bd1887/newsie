from django.core.management.base import BaseCommand
from newsie.scripts.merge_clusters import merge_clusters

class Command(BaseCommand):
    help = 'Recluster all articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Merging article topics...")
        merge_clusters()
        self.stdout.write("Done!")

    
