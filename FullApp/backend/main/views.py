from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Page was found: Home</h1>")

def about(request):
    return HttpResponse("this is a about view")

def contact(request):
    return HttpResponse("this is a contact view")