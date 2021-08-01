# accounts/urls.py
from django.urls import path
from .views import Actions

urlpatterns = [
    path('', Actions.as_view(), name='actions'),
]