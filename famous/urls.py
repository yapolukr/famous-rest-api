from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('about/', about, name ='about'),
    path('contact/', contact, name ='contact'),

]