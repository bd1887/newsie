from django.core.management.base import BaseCommand
from django.db.models import Max
from newsie.models import Article
from newsie.publications import get_articles
from newsie.nlp.dbscan import dbscan
from newsie.nlp.tokenize import tokenize
from newsie.publications import get_articles
import datetime
from django.utils import timezone

from gensim.parsing.preprocessing import remove_stopwords
from gensim.models import Phrases
from gensim.models.phrases import Phraser
import nltk, re, string, collections
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from gensim.utils import lemmatize


class Command(BaseCommand):
    help = 'Create new tokens for articles'

    def handle(self, *args, **kwargs):
        self.stdout.write("Retokenizing...")
        self.tokenize()
        self.stdout.write("Done!")

    def tokenize(self):

        range_start = datetime.datetime.combine(datetime.date.today() - datetime.timedelta(days=365), datetime.time.min, timezone.utc)
        range_end = datetime.datetime.combine(datetime.date.today(), datetime.time.max, timezone.utc)

        for topic in get_articles.topics():
            query_set = Article.objects.filter(pub_date__range=(range_start, range_end), category__exact=topic)
            
            tokenized_articles = tokenize(query_set)

            for article in tokenized_articles:
                article.save()