from django.urls import path
from .views import register, login_request

urlpatterns = [
    path('', register, name='register'),
    path('', login_request, name='login'),
]
