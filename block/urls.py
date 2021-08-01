# accounts/urls.py
from django.urls import path
from .views import BlockList

urlpatterns = [
    path('', BlockList.as_view(), name='block'),
]