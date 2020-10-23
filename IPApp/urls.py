from django.contrib import admin
from django.urls import path

from .views import index, finder

urlpatterns = [
    path('', index, name='home'),
    path('/find/', finder, name='finder')
]