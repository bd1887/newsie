from django.core.management.base import BaseCommand
from newsie.scripts.test_manual import test_manual

class Command(BaseCommand):
    help = 'Tests the currently trained classifier against manually labeled data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Testing...")
        test_manual()
        self.stdout.write("Done!")

    
