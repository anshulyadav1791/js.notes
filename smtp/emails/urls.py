from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_test, name='send_test_email'),
]
