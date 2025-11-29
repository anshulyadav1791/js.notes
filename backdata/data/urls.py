from django.urls import path
from .views import data_create, data_list, data_detail, data_edit,data_delete

app_name = "backdata"   # <<-- ADD THIS

urlpatterns = [
    path('', data_create, name='data_create'),
    path('list/', data_list, name='data_list'),
    path('detail/<int:pk>/', data_detail, name='data_detail'),
    path("edit/<int:pk>/", data_edit, name="data_edit"),
    path("delete/<int:pk>/", data_delete, name="data_delete"),
]
