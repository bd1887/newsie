from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from newsie.models import Article, ArticleCluster
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import APIException

class ExclusiveStoriesView(generics.ListAPIView):
    # Instructs how to serialize the model to JSON:
    serializer_class = serializers.ArticleClusterSerializer

    # Allows for calls such as "/api/exclusive-stories/?limit=20&offset=0"
    # to return only the first 20 results
    pagination_class = LimitOffsetPagination

    # Called by default when a GET request is made to this view:
    def get_queryset(self):
        # Extracts category filters from query parameters:
        categories = self.request.query_params.get('categories')

        # Filters out any stories which were "Top Stories" within the last 3 hours
        # to prevent redundant stories between the two views.
        last_36_hours = timezone.make_aware(datetime.today() - timedelta(hours=36))
        queryset = ArticleCluster.objects.exclude(top_story_on__gte=last_36_hours).order_by('-most_recent_pub_date', '-size_today', '-size', 'id')

        # Extracts categories in the query parameters (if any) and filters accordingly
        if categories is not None:
            filtered_queryset = ''
            filters_array = categories.split(',')
            queryset = queryset.filter(category__in=filters_array)

        return queryset


class TopStoriesView(generics.ListAPIView):
    # Called by default:
    def list(self, request):

        # A dictionary of valid date range queries
        # and their corresponding size attributes
        valid_date_range_queries = {
            '': 'size_today',
            'today': 'size_today',
            'this_week': 'size_this_week',
            'this_month': 'size_this_month',
            'all_time': 'size',
        }

        # Extracts 'date_range' parameter from query
        date_range_query = request.GET.get('date_range', '')
        date_range_string = ''

        # Checks query parameter value against dictionary of valid values and gets the corresponding size attribute
        try:
            date_range_string = valid_date_range_queries[date_range_query]
        except:
            # Invalid date_range query parameter value
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Gets queryset and serializes it
        queryset = self.get_queryset(date_range=date_range_string)
        serializer = serializers.ArticleClusterSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, date_range=''):
        # Creates the "order_by" string: defaults to "-size_today"
        order_by_string = f"-{date_range}" if date_range != '' else "-size_today"

        # "Top Stores" are the largest 15 clusters within the given date range with at least 2 Articles
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