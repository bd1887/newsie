from django.core.management.base import BaseCommand
from newsie.scripts.find_top_stories import find_top_stories

class Command(BaseCommand):
    help = 'Finds todays top stories'

    def handle(self, *args, **kwargs):
        self.stdout.write("Finding today's top stories")
        find_top_stories()
        self.stdout.write("Done!")
