from django.core.management.base import BaseCommand
from newsie.scripts.plot_nn import plot_nn

class Command(BaseCommand):
    help = 'Creates a plot of the third nearest neighbor of each Article object for determining an optimal epsilon value for the dbscan clustering algorithm'

    def handle(self, *args, **kwargs):
        self.stdout.write("Finding nearest neighbors...")
        plot_nn()
        self.stdout.write("Done!")

    
