from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib import admin
# Create your models here.

class Article(models.Model):
    url = models.URLField(unique=True)
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

    # tokens = ArrayField(
    #     models.CharField(max_length=5000),
    #     blank=True,
    #     default=list()
    #     )

    def __str__(self):
        category_string = self.category if self.category != '' else "Not Categorized"
        return "{0} - {1} - {2}".format(self.id, category_string, self.title)

    def get_text(self):
        desc = "" if self.description == None else self.description
        return "{0} {1} {2}".format(self.title, desc, self.body)

    def to_dict(self):
        return {
            'url': self.url,
            'text': self.get_text(),
            'category': self.category,
        }

admin.site.register(Article)