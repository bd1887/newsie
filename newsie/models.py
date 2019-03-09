from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin

class Article(models.Model):
    url = models.URLField(max_length=500, unique=True)
    title = models.CharField(max_length=500)
    authors = ArrayField(
        models.CharField(max_length=500),
        blank=True,
        default=list
        )
    body = models.TextField(blank=True)
    description = models.CharField(max_length=1000, blank=True, default='')
    category = models.CharField(max_length=500, blank=True)
    img = models.URLField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now, blank=True)
    tokens = ArrayField(
        models.CharField(max_length=500),
        blank=True,
        default=list
    )
    topic_id = models.IntegerField(blank=True, null=True)
    labeled = models.BooleanField(default=True)

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
            'url': self.url,
            'text': self.tokens,
            'category': self.category,
        }

admin.site.register(Article)