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
        'title': 'Main page',
        'cat_selected': 0,
    }

    return render(request, 'famous/index.html', context=context)

def about(request):
    return render(request, 'famous/about.html', { 'menu':menu, 'title':'Main page'})

def show_category(request, cat_id):
    posts = Famous.objects.filter(cat_id=cat_id)


    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Display by categories',
        'cat_selected': cat_id,
    }

    return render(request, 'famous/index.html', context=context)

def show_post(request, post_id):
    return HttpResponse (f'{post_id}')


def contact(request):
    return HttpResponse("Contact us")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found<h1/>')