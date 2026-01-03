from django.urls import path
from .import views

urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('data/', views.users_data, name='users_data'),

]
