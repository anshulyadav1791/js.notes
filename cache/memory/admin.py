from django.contrib import admin
from .models import YouTubeUser, UserData


@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subscribers')


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subscribers')
