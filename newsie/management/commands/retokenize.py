from django.core.management.base import BaseCommand
from newsie.scripts.retokenize import retokenize

class Command(BaseCommand):
    help = 'Performs preprocessing on all Article objects and updates their tokens attribute'

    def handle(self, *args, **kwargs):
        self.stdout.write("Retokenizing...")
        retokenize()
        self.stdout.write("Done!")

    
