from django.core.management.base import BaseCommand
from django.db.models import Max
from newsie.models import Article
from newsie.publications import get_articles
from newsie.nlp.category_classifier import train
from newsie.nlp.dbscan import dbscan
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help = 'Runs all necessary scheduled tasks.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Getting todays' news articles. This may take several minutes...")
        self.update_articles()

        self.stdout.write("Training topic classifier...")
        self.train_classifier()

        self.stdout.write("Merging article topics...")
        self.merge_stories()

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

    def train_classifier(self):
        articles = Article.objects.all().exclude(labeled__exact=False, category__exact='')
        train(articles)

    def merge_stories(self):

        range_start = datetime.datetime.combine(datetime.date.today() - datetime.timedelta(days=365), datetime.time.min, timezone.utc)
        range_end = datetime.datetime.combine(datetime.date.today(), datetime.time.max, timezone.utc)

        for category in get_articles.categories():
            query_set = Article.objects.filter(pub_date__range=(range_start, range_end), category__exact=category)
            sorted_query_set = dbscan(query_set)
            
            for topic in sorted_query_set:
                lowest_topic_id = self.get_next_id()

                for article in topic:
                    if article.topic_id != None and article.topic_id < lowest_topic_id:
                        lowest_topic_id = article.topic_id
                
                for article in topic:
                    article.topic_id = lowest_topic_id
                    article.save()

    def get_next_id(self):
        max_topic_id = Article.objects.all().aggregate(Max('topic_id'))['topic_id__max']
        next_topic_id = 1 if max_topic_id == None else max_topic_id + 1
        return next_topic_id