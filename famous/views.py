from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    posts = Famous.objects.all()
    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected': 0,
    }
    return render(request, 'famous/index.html', context=context)

def about(request):
    return render(request, 'famous/about.html')

def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Famous.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        raise Http404

    context = {
        'posts': posts,
        'title': 'Display by categories',
        'cat_selected': cat[0].id,
    }

    return render(request, 'famous/index.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Famous, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'famous/post.html', context=context)

def contact(request):
    return render(request, "famous/contact.html")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found<h1/>')