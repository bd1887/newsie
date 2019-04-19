from django.db.models import Count
from newsie.models import ArticleCluster
from datetime import datetime, timedelta
from django.utils import timezone

def clean_clusters():
        empty_clusters = ArticleCluster.objects.annotate(article_count=Count('articles')).filter(article_count=0)
        for cluster in empty_clusters:
            cluster.delete()

        today = timezone.make_aware(datetime.today())
        one_week_ago = today - timedelta(days=7)
        unimportant_clusters = ArticleCluster.objects.filter(top_story_on=None, most_recent_pub_date__lte=one_week_ago)

        for cluster in unimportant_clusters:
            cluster.delete()