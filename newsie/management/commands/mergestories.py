from django.core.management.base import BaseCommand
from django.db.models import Max
from newsie.models import Article
from newsie.publications import get_articles
from newsie.nlp.dbscan import dbscan
from newsie.publications import get_articles
import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = 'Gets todays top stories'

    def handle(self, *args, **kwargs):
        self.stdout.write("Merging stories...")
        self.merge_stories()
        self.stdout.write("Done!")

    def merge_stories(self):

        range_start = datetime.datetime.combine(datetime.date.today() - datetime.timedelta(days=365), datetime.time.min, timezone.utc)
        range_end = datetime.datetime.combine(datetime.date.today(), datetime.time.max, timezone.utc)

        for topic in get_articles.topics():
            query_set = Article.objects.filter(pub_date__range=(range_start, range_end), category__exact=topic)
            sorted_query_set = dbscan(query_set)
            
            for story in sorted_query_set:
                lowest_story_id = self.get_next_id()

                for article in story:
                    if article.story_id != None and article.story_id < lowest_story_id:
                        lowest_story_id = article.story_id
                
                for article in story:
                    article.story_id = lowest_story_id
                    article.save()

    def get_next_id(self):
        max_story_id = Article.objects.all().aggregate(Max('story_id'))['story_id__max']
        next_story_id = 1 if max_story_id == None else max_story_id + 1
        return next_story_id
