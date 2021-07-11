# posts/urls.py
from django.urls import path
from .views import HomePageView, create_post, post_view, post_detail_page, chingachung, Quizzes, theme_selection

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', create_post, name='post'),
    path('view_posts/', post_view, name='post_view'),
    path('post/<int:pk>/', post_detail_page, name='post_detail_page'),
    path('Quizzes/', Quizzes, name='Quizzes'),
    path('chingachung/', chingachung, name='chingachung'),
    path('theme_selection/',theme_selection, name='theme_selection'),
]
