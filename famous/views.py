from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add post", 'url_name': 'add_page'},
        {'title': "Contact", 'url_name': 'contact'},
        {'title': "Sogn In", 'url_name': 'login'}
]


def index(request):
    posts = Famous.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page'
    }

    return render(request, 'famous/index.html', context=context)

