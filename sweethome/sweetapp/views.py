from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Max
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .models import *
from .utils import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Аренда", 'url_name': 'home'},
        {'title': "Продажа", 'url_name': 'home'},
        {'title': "Новостройки", 'url_name': 'home'},
        {'title': "Ипотека", 'url_name': 'home'},

]

def contact(request):
    return HttpResponseNotFound('Обратная связь')

class SweetHome(TemplateView):
    template_name = "sweetapp/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SweetHome, self).get_context_data(*args, **kwargs)
        context['title'] = "Главная страница"
        context['menu'] = menu
        context['news'] = News.objects.all()[0:3]
        context['specialists'] = Specialist.objects.all()[0:3]
        context['companies'] = Company.objects.all()[0:3]
        return context



class ShowNews(DetailView):
    model = News
    template_name = 'sweetapp/news.html'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = context['news']
        context['menu'] = menu
        return context
