from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    url(r'^top-stories', views.TopStoriesView.as_view()),
    url(r'^exclusive-stories', views.ExclusiveStoriesView.as_view()),
]