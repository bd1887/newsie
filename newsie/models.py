from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin
from urllib.parse import urlparse
import re

class ArticleCluster(models.Model):
    size = models.IntegerField(default=0)
    size_this_month = models.IntegerField(default=0)
    size_this_week = models.IntegerField(default=0)
    size_today = models.IntegerField(default=0)
    top_story_on = models.DateTimeField(null=True)

    most_recent_pub_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=1000, blank=True)

    def update_metadata(self):
        cluster_articles = Article.objects.filter(cluster__id=self.id)
        self.update_size(cluster_articles)
        self.update_category(cluster_articles)
        self.update_most_recent_pub_date(cluster_articles)
        self.save()

    def update_size(self, cluster_articles):
        # Set total size
        self.size = len(cluster_articles) if cluster_articles is not None else 0

        # Today and time deltas
        now = timezone.now()
        one_day = timezone.timedelta(hours=36)
        one_week = timezone.timedelta(days=7)
        one_month = timezone.timedelta(days=31)
        
        # Find articles within the given date ranges
        articles_this_month = [article for article in cluster_articles if article.pub_date > (now - one_month)]
        articles_this_week = [article for article in articles_this_month if article.pub_date > (now - one_week)]
        articles_today = [article for article in articles_this_week if article.pub_date > (now - one_day)]

        # Set the sizes within the given date ranges
        self.size_this_month = len(articles_this_month)
        self.size_this_week = len(articles_this_week)
        self.size_today = len(articles_today)

    def update_most_recent_pub_date(self, cluster_articles):
        self.most_recent_pub_date = max(article.pub_date for article in cluster_articles) if cluster_articles is not None else ''

    def update_category(self, cluster_articles):
        self.category = cluster_articles[0].category if cluster_articles is not None else None

    def __str__(self):
        category_string = self.category if self.category != '' else "Not Categorized"
        return f"{self.id} - {self.category} - {self.size} - {self.most_recent_pub_date}"


class Article(models.Model):
    url = models.URLField(max_length=1000, unique=True)
    title = models.CharField(max_length=1000)

    #A PostgreSQL-specific field that stores lists
    authors = ArrayField( 
        models.CharField(max_length=1000), #Stores a list of Charfields
        blank=True,
        default=list
        )

    #Text from the Article's body
    body = models.TextField(blank=True)

    #RSS feeds usually include descriptions of articles
    description = models.CharField(max_length=1000, blank=True, default='')

    #Category of RSS feed if labeled,
    # otherwise the category predicted by the classifier
    category = models.CharField(max_length=1000, blank=True)

    #Img url
    img = models.URLField(max_length=1000, blank=True)

    #Date of publication
    pub_date = models.DateTimeField(default=timezone.now, blank=True)

    #Article text, preprocessed and tokenized
    tokens = ArrayField(
        models.CharField(max_length=1000),
        blank=True,
        default=list
    )

    # Foreign key of associated cluster
    cluster = models.ForeignKey(ArticleCluster, on_delete=models.CASCADE, null=True, blank=True, related_name="articles")

    #Article came from a labeled RSS feed?
    labeled = models.BooleanField(default=True)
    
    # Manually applied label for testing purposes
    manual_label = models.CharField(max_length=1000, blank=True)


# Simply to appease the linter:
    id = ''
    objects = models.Manager()
###############################

    def __str__(self):
        category_string = self.category if self.category != '' else "Not Categorized"
        return f"{self.id} - {category_string} - {self.title}"

    def get_text(self):
        desc = "" if self.description == None else self.description
        return f"{self.title} {desc} {self.body}"

    def to_dict(self):
        return {
            'url_tokens': re.split('/|-', urlparse(self.url).path.split('.')[0])[1:],
            'tokens':  self.tokens,
            'category': self.category,
        }

admin.site.register(Article)
admin.site.register(ArticleCluster)