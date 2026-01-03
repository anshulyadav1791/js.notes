from django.shortcuts import render
from .models import YouTubeUser, UserData
from django.core.cache import cache
from django.views.decorators.cache import cache_page



def users_list(request):
    users = cache.get('users_data')

    if users is None:
        print('cache miss: data from database')
        users = list(YouTubeUser.objects.all())
        cache.set('users_data', users, timeout=60)
    else:
        print('cache hit: fetching data from cache')

    return render(request, 'users_list.html', {'users': users})


def users_data(request):
    users = cache.get('users_list')

    if not users:
        print("cache miss: querying database for users.")
        users = UserData.objects.all()
        cache.set('user_list', users, timeout=60)
    else:
        print('Cahe hit: retrieved users from cache.')

    return render(request, 'users_data.html', {'data': users})
