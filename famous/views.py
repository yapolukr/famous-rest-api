from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Contact", 'url_name': 'contact'},
]

def index(request):
    posts = Famous.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page'
    }

    return render(request, 'famous/index.html', context=context)

def about(request):
    return render(request, 'famous/about.html', { 'menu':menu, 'title':'Main page'})

def categories(request):
    return render(request, 'famous/categories.html')


def contact(request):
    return HttpResponse("Contact us")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found<h1/>')