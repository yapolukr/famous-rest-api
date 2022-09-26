from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView
from rest_framework import generics

from .serializers import FamousSerializer


class FamousHome(ListView):
    model = Famous
    template_name = 'famous/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['cat_selected'] = 0
        return context

class FamousCat(ListView):
    model = Famous
    template_name = 'famous/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Famous.objects.filter(cat__slug=self.kwargs['cat_slug'])


def about(request):
    return render(request, 'famous/about.html')


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

class FamousAPIView(generics.ListAPIView):
    queryset = Famous.objects.all()
    serializer_class = FamousSerializer

