from django.db.models import Count
from newsie.models import Article
from datetime import datetime, timedelta
from django.utils import timezone

def clear_old_articles():
        today = timezone.make_aware(datetime.today())
        one_week_ago = today - timedelta(days=7)
        old_articles = Article.objects.filter(pub_date__lte=one_week_ago)
        for article in old_articles:
            article.delete()