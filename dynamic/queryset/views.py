from django.shortcuts import render
from django.db.models import Q
from .models import Post   # ✅ THIS LINE WAS MISSING


def post_list(request):
    query = request.GET.get('q')
    catagory = request.GET.get('catagory')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    if catagory:
        posts = posts.filter(catagory__iexact=catagory)  # ✅ FIXED

    return render(request, 'dynamic/post_list.html', {
        'posts': posts,
        'query': query,
        'catagory': catagory,
    })
