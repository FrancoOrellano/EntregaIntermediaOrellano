from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def about_me(request):
    return render(request, 'about_me.html', context={})