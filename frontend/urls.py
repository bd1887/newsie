from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.index),
    path('top-stories/', views.index),
    path('exclusive-stories/', views.index),
]
