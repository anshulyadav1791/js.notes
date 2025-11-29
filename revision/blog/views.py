# from django.shortcuts import render


# def blog(request):
#     def blog(requset):
#         return render(request, 'blog.html')

from django.shortcuts import render

def blog(request):
    return render(request, 'blog.html')
