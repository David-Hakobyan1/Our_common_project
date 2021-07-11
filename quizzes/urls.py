# posts/urls.py
from django.urls import path
from .views import quizzes, chingachung, subjects, play

urlpatterns = [
    path('', quizzes, name='quizzes'),
    path('chingachung/', chingachung, name='chingachung'),
    path('subjects/', subjects, name='subjects'),
    path('play/<int:index>', play, name='play'),
]
