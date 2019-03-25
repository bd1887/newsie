from django.core.management.base import BaseCommand
from django.db.models import Max
from newsie.models import Article

class Command(BaseCommand):
    help = 'Clear all stories'

    def handle(self, *args, **kwargs):
        self.stdout.write("Clearing stories...")
        self.clear_stories()
        self.stdout.write("Done!")

    def clear_stories(self):
        for article in get_articles.topics():
            query_set = Article.objects.all()
            for article in query_set:
                article.story_id = None
                article.save()