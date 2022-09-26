from django.urls import path
from famous.views import FamousAPIView
from .views import *

urlpatterns = [
    path('', FamousHome.as_view(), name='home'),
    path('category/<slug:cat_slug>/', FamousCat.as_view(), name='category'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('about/', about, name ='about'),
    path('contact/', contact, name ='contact'),
    path('api/v1/famouslist/', FamousAPIView.as_view()),

]