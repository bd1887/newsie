from newsie.models import ArticleCluster
from datetime import datetime, timedelta
from django.utils import timezone
from newsie.publications.get_articles import categories

def find_top_stories():
        for category in categories(): #Iterate through RSS feed Categories

            #Get today's stories
            today = timezone.make_aware(datetime.today())
            last_36_hours = timezone.make_aware(datetime.today() - timedelta(hours=36))

            # Find top 5 clusters if size is 2 or greater
            top_stories = ArticleCluster.objects \
            .filter(most_recent_pub_date__gte=last_36_hours, category__exact=category, size__gte=2) \
            .order_by('-size')[:5]

            for cluster in top_stories:
                cluster.top_story_on = today
                cluster.save()