from django.urls import path
from .import views

urlpatterns = [
    path('', views.twitter_home, name='twitter-home')
]