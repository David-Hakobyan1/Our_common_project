# posts/urls.py
from django.urls import path
from .views import HomePageView, create_post

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', create_post, name='post'),
    ]
