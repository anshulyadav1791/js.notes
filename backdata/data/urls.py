from django.urls import path
from .views import data_create, data_list, data_detail

urlpatterns = [
    path('', data_create, name='data_create'),
    path('list/', data_list, name='data_list'),
    path('detail/<int:pk>/', data_detail, name='data_detail'),
]
