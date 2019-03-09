from django.core.management.base import BaseCommand
from django.db.models import Max
from newsie.models import Article
from newsie.publications import get_articles

class Command(BaseCommand):
    help = 'Runs webscraper'

    def handle(self, *args, **kwargs):
        self.stdout.write("Getting todays' news articles. This may take several minutes...")
        self.update_articles()
        self.stdout.write("Done!")

    def update_articles(self):
        new_articles = get_articles.update()

        for art in new_articles:
            db_art, created = Article.objects.get_or_create(url=art.url)
            if created:
                db_art.title = art.title
                db_art.body = art.body
                db_art.description = art.description
                db_art.img = art.img
                db_art.pub_date = art.pub_date
                db_art.category = art.category
                db_art.tokens = art.tokens
                db_art.save()
