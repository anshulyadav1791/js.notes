from django.urls import path, include
from .views import CourseViewSet
from .models import Course
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls))
]

