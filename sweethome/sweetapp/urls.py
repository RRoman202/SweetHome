from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', SweetHome.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),


]