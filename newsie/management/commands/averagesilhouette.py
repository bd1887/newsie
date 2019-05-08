from django.core.management.base import BaseCommand
from newsie.scripts.average_silhouette import average_silhouette

class Command(BaseCommand):
    help = 'Prints the top silhouette scores of DBSCAN clusters with various epsilon values for each category and prints the average top score'

    def handle(self, *args, **kwargs):
        self.stdout.write("Calculating silhouette score...")
        average_silhouette()
        self.stdout.write("Done!")

    
