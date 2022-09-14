from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('about/', about, name ='about'),
    path('contact/', contact, name ='contact'),

]