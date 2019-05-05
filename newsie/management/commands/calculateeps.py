from django.core.management.base import BaseCommand
from newsie.scripts.calculate_eps import calculate_eps

class Command(BaseCommand):
    help = 'Creates KNN plot for determining optimal eps for dbscan clustering'

    def handle(self, *args, **kwargs):
        self.stdout.write("Calculating eps...")
        calculate_eps()
        self.stdout.write("Done!")