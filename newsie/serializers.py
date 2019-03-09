from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'url', 'title', 'description', 'category', 'img', 'pub_date', 'topic_id', 'labeled')


class ResultsField(serializers.ListSerializer):
    child = serializers.ListField(
        child = ArticleSerializer()
    )


class TopicsSerializer(serializers.Serializer):
    sports = ResultsField()
    business_and_finance = ResultsField()
    entertainment = ResultsField()
    health = ResultsField()
    education = ResultsField()
    ireland = ResultsField()
    world = ResultsField()