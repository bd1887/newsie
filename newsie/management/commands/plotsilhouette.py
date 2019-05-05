from django.core.management.base import BaseCommand
from newsie.scripts.plot_silhouette import plot_silhouette

class Command(BaseCommand):
    help = 'Creates a plot of the silhouette scores of DBSCAN clusters with various epsilon values'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating silhouette score plot...")
        plot_silhouette()
        self.stdout.write("Done!")

    
