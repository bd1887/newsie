from django.core.management.base import BaseCommand
from newsie.models import Article
from newsie.publications.get_articles import categories

class Command(BaseCommand):
    help = 'Runs webscraper'

    def handle(self, *args, **kwargs):
        self.stdout.write("Cleaning category models... ")
        self.clean_categories()
        self.stdout.write("Done!")

    def clean_categories(self):
        cats = categories()
        articles = Article.objects.all().exclude(category__in=cats)

        for art in articles:
            art.category = ''
            art.save()
