from rest_framework import viewsets, generics
from rest_framework.response import Response
from . import serializers
from newsie.models import Article
from newsie.nlp.dbscan import dbscan
from newsie.publications.get_articles import categories
from utils.get_date_or_default import get_date_or_default
from django.db.models import Count


class TopStoriesView(generics.ListAPIView):
    serializer_class = serializers.TopicsSerializer

    def list(self, request):

        #Extract dates from GET query
        range_start = get_date_or_default(request.GET.get('range_start'), default="yesterday_min")
        range_end = get_date_or_default(request.GET.get('range_start'), default="today_max")

        queryset = self.get_queryset(range_start=range_start, range_end=range_end)
        serializer = serializers.TopicsSerializer(queryset)
        return Response(serializer.data)

    def get_queryset(self, range_start, range_end):
        query_dict ={}
        
        for category in categories(): #Iterate through RSS feed Categories

            # Find topics with the most articles in them if the number of topics is greater than 1:
            query = Article.objects \
            .filter(pub_date__range=(range_start, range_end), category__exact=category) \
            .values_list('topic_id').annotate(article_count=Count('topic_id')) \
            .filter(article_count__gt=1).order_by('-article_count')

            query = query[:3] #Get three most common topics in each category

            query_set = []
            for topic in query:
                # Get the articles with the common topic ids calculated above
                bucket = Article.objects.filter(pub_date__range=(range_start, range_end), category__exact=category, topic_id__exact=topic[0]).order_by('pub_date')
                query_set.append(bucket)

            category = category.lower().replace(' ', '_') #Make category name JSON-friendly
            
            query_dict[category]=query_set

        return query_dict

class ExclusiveStoriesView(generics.ListAPIView):

    def list(self, request):

        #Extract dates from GET query
        range_start = get_date_or_default(request.GET.get('range_start'), default="today_min")
        range_end = get_date_or_default(request.GET.get('range_start'), default="today_max")

        queryset = self.get_queryset(range_start, range_end)
        serializer = serializers.TopicsSerializer(queryset)
        return Response(serializer.data)

    def get_queryset(self, range_start, range_end):

        query_dict ={}

        for category in categories(): #Iterate through RSS feed Categories

            # Find topics with the most articles in them:
            topics = Article.objects \
            .filter(pub_date__range=(range_start, range_end), category__exact=category) \
            .values_list('topic_id').annotate(article_count=Count('topic_id')) \
            .order_by('-article_count')
            
            topics = topics[3:] #Remove the three most common topics (These will appear in the top stories)

            query_set = []
            for topic in topics:
                # Get the articles with the common topic ids calculated above
                bucket = Article.objects.filter(pub_date__range=(range_start, range_end), category__exact=category, topic_id__exact=topic[0])
                query_set.append(bucket)

            category = category.lower().replace(' ', '_') #Make category name JSON-friendly
            
            query_dict[category]=query_set

        return query_dict