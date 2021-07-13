# posts/urls.py
from django.urls import path
from .views import HomePageView, create_post, post_view, post_detail_page, PostUpdateView, PostDeleteView, add_dislike, add_like

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', create_post, name='post'),
    path('view_posts/', post_view, name='post_view'),
    path('post/<int:pk>/', post_detail_page, name='post_detail_page'),
    path('post/<int:pk>/like', add_like, name='like'),
    path('post/<int:pk>/dislike', add_dislike, name='dislike'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
