# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.blog, name='blog'),
# ]
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
]
