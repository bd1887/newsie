from django.core.management.base import BaseCommand
from newsie.scripts.clear_old_articles import clear_old_articles

class Command(BaseCommand):
    help = 'Clears articles more than one week old'

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing old articles...")
        clear_old_articles()
        self.stdout.write("Done!")
