from rest_framework import serializers
from .models import Article, ArticleCluster
from rest_framework.utils.urls import replace_query_param

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'description', 'category', 'img', 'pub_date', 'labeled')

class ArticleClusterSerializer(serializers.ModelSerializer):
    # Calls self.get_articles() (the default name) to add related articles as a field:
    articles = serializers.SerializerMethodField()
    class Meta:
        model = ArticleCluster
        fields = ('id', 'category', 'size' ,'size_today', 'size_this_week','size_this_month', 'most_recent_pub_date', 'articles')

    def get_articles(self, instance):
        # Get related articles; order_by most recent first
        articles = Article.objects\
            .filter(cluster__id=instance.id)\
            .order_by('-pub_date')

        article_serializer = ArticleSerializer(articles, many=True)
        return article_serializer.data


class ResultsField(serializers.ListSerializer):
    child = serializers.ListField(
        child = ArticleSerializer()
    )

class TopicsSerializer(serializers.Serializer):
    sports = ArticleClusterSerializer(many=True, read_only=True)
    business_and_finance = ArticleClusterSerializer(many=True, read_only=True)
    entertainment = ArticleClusterSerializer(many=True, read_only=True)
    health = ArticleClusterSerializer(many=True, read_only=True)
    education = ArticleClusterSerializer(many=True, read_only=True)
    ireland = ArticleClusterSerializer(many=True, read_only=True)
    world = ArticleClusterSerializer(many=True, read_only=True)

class EndpointSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=500)
    url = serializers.URLField()
    parameters = serializers.ListField(
        child = serializers.CharField(max_length=500)
    )

class InstructionsSerializer(serializers.Serializer):
    instructions = serializers.ListField(
        child = EndpointSerializer()
    )