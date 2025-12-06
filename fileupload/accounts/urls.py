from django.urls import path
from . import views   # <-- add a space between '.' and 'import'

urlpatterns = [
    path('upload/', views.uploade_profile, name='upload_profile'),
    path('profile/', views.view_profile, name='view_profile'),
]
