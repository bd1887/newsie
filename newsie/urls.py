from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # url('sorted/', views.SortedArticles.as_view()),
    url(r'^articles', views.ArticleView.as_view()),
    path('update/', views.update_articles),
    path('category/', views.update_categories),
    path('train/', views.train_classifier),
    path('classify/', views.classify_article),
]