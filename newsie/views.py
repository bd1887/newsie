from rest_framework import generics
from rest_framework.response import Response
from . import serializers
from newsie.models import Article, ArticleCluster
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import APIException

class ExclusiveStoriesView(generics.ListAPIView):
    last_36_hours = timezone.make_aware(datetime.today() - timedelta(hours=36))
    queryset = ArticleCluster.objects.exclude(top_story_on__gte=last_36_hours).order_by('-most_recent_pub_date', 'id')
    serializer_class = serializers.ArticleClusterSerializer
    pagination_class = LimitOffsetPagination


class TopStoriesView(generics.ListAPIView):

    def list(self, request):

        valid_date_range_queries = {
            '': 'size_today',
            'today': 'size_today',
            'this_week': 'size_this_week',
            'this_month': 'size_this_month',
            'all_time': 'size',
        }
        date_range_query = request.GET.get('date_range', '')
        date_range_string = ''

        try:
            date_range_string = valid_date_range_queries[date_range_query]
        except:
            raise InvalidQueryError()

        queryset = self.get_queryset(date_range=date_range_string)
        serializer = serializers.ArticleClusterSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, date_range=''):
        order_by_string = f"-{date_range}" if date_range != '' else "-size_today"
        queryset = ArticleCluster.objects.filter(size__gte=2).order_by(order_by_string)[:15]

        return queryset

class InstructionsView(generics.GenericAPIView):
    serializer_class = serializers.InstructionsSerializer

    def get(self, request):

        top_stories_instructions = {
            'name': '/top-stories',
            'url': 'https://bd1887-newsie.herokuapp.com/top-stories',
            'parameters': [
                'date_range=[today, this_week, this_month, all]'
            ],
        }
        exclusive_stories_instructions = {
            'name': '/exclusive-stories',
            'url': 'https://bd1887-newsie.herokuapp.com/exclusive-stories',
            'parameters': [
                'limit=#',
                'offset=#'
            ]
            
        }

        instructions = {
            'instructions': [
                top_stories_instructions,
                exclusive_stories_instructions,
            ]
        }

        serializer = serializers.InstructionsSerializer(instructions)
        return Response(serializer.data)