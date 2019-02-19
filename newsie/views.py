from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from . import serializers
from newsie.models import Article
from newsie.nlp.dbscan import dbscan
from newsie.nlp.topic_classifier import train, classify
import datetime
from newsie.publications.news_please_test import news_plz

# For /update
from newsie.publications import get_articles

def train_classifier(request):
    html = ""
    arts = Article.objects.all().exclude(category__exact='')

    resp = train(arts)

    for art in arts:
        html += art.category + "</br>"

    return HttpResponse(resp.to_html())

def classify_article(request):
    html = ""
    arts = Article.objects.all().filter(category__exact='')

    for art in arts:
        html_string = classify(art)
        html += html_string
    
    return HttpResponse(html)



def update_categories(request):
    html = ""
    cat_string = "courts"
    category = "Crime and Law"
    arts = Article.objects.all()

    html += "Total number of articles" + str(len(arts)) + "</br></br>"

    counter = 0

    for art in arts:
        if art.url.find(cat_string) >= 0:
            counter += 1
            html += str(art.id) +" " + art.url + "</br>"
            art.category = category
            art.save()

    html = "Articles with string '" + cat_string +"' " + str(counter) + "</br>" + html

    return HttpResponse(html)


def update_articles(request):
    html = ""
    new_articles = get_articles.update()
    for art in new_articles:
        db_art, created = Article.objects.get_or_create(url=art.url)
        html += "<p>%s</p></br>" % art.title
        
        db_art.title = art.title
        db_art.body = art.body
        db_art.description = art.description
        db_art.img = art.img
        db_art.pub_date = art.pub_date
        db_art.category = art.category
        db_art.save()
    
    return HttpResponse(html)

class ArticleView(generics.ListAPIView):
    
    serializer_class = serializers.ResultsField

    def list(self, request):
        is_sorted = True if request.GET.get('sorted') == 'true' else False

        date_format_url = "%Y-%m-%d"
        date_format_tz = "%Y-%m-%d %H:%M:%S%z"

        range_start = request.GET.get('range_start')
        range_end = request.GET.get('range_end')
        try:
            range_start = datetime.datetime.strptime(range_start, date_format_url)
            range_start = datetime.datetime.combine(range_start, datetime.time.min, timezone.utc)
        except Exception as e:
            print(e)
            range_start = datetime.datetime.combine(datetime.date.today(), datetime.time.min, timezone.utc)
        try:
            range_end =  datetime.datetime.strptime(range_end, date_format_url)
            range_end = datetime.datetime.combine(range_end, datetime.time.min, timezone.utc)
        except:
            print("range_end exception")
            range_end = datetime.datetime.combine(datetime.date.today(), datetime.time.max, timezone.utc)
        
        queryset = self.get_queryset(is_sorted=is_sorted, range_start=range_start, range_end=range_end)
        serializer = serializers.ResultsField(queryset) if is_sorted else serializers.ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, is_sorted=False, range_start=None, range_end=None):
        is_sorted = is_sorted
        queryset = None

        query_set = Article.objects.filter(pub_date__range=(range_start, range_end))
        print("Total Articles: ", len(query_set))
        if (is_sorted):
            sorted_set = dbscan(query_set)
            counter = 0
            for art_list in sorted_set:
                if len(art_list) > 1:
                    counter += len(art_list)
            print("Sorted articles: ", counter)
            return sorted_set
        else:
            return query_set

# class SortedArticles(viewsets.ViewSet):
#     def list(self, request):
#         queryset = self.test_meth()
#         # serializer = serializers.TestModelSerializer(queryset, many=True)
#         return Response(queryset)

#     def test_meth(self):
#         return [
#             [model_to_dict(TestModel(id=1, name='one')), model_to_dict(TestModel(id=2, name='two'))],
#             [model_to_dict(TestModel(id=3, name='three'))]
#             ]