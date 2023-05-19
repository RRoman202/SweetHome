from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Max
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from .forms import *
from .models import *
from .utils import *

menu = [{'title': "Главная", 'url_name': 'home'},
        {'title': "Аренда", 'url_name': 'rent'},
        {'title': "Продажа", 'url_name': 'kupit'},
        {'title': "Новостройки", 'url_name': 'newbuilding'},
        {'title': "Ипотека", 'url_name': 'calculator'},

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
        context['offers'] = Offer.objects.all()[0:4]
        context['reviews'] = Review.objects.all()[0:5]
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



class RegisterUser(CreateView):
    form_class = RegisterUserForm

    template_name = 'sweetapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['menu'] = menu

        return context

    def form_valid(self, form):
        user = form.save()


        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'sweetapp/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        context['menu'] = menu
        return context

    def get_success_url(self):
        return reverse_lazy('home')

class NewBuildingKatalog(ListView):
    paginate_by = 3
    model = Newbuilding
    template_name = 'sweetapp/newbuilding.html'
    context_object_name = 'buildings'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новостройки'
        context['menu'] = menu
        return context

class PersonView(TemplateView):
    template_name = 'sweetapp/person.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Личный кабинет'
        context['menu'] = menu
        return context

class RentView(ListView):
    paginate_by = 3
    model = Rent
    template_name = 'sweetapp/rent.html'
    context_object_name = 'rents'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Аренда'
        context['menu'] = menu
        return context

class KupitKatalog(ListView):
    paginate_by = 6
    model = Estate
    template_name = 'sweetapp/kupit.html'
    context_object_name = 'estates'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продажа'
        context['menu'] = menu
        return context

class CalculatorView(TemplateView):
    template_name = "sweetapp/calculator.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CalculatorView, self).get_context_data(*args, **kwargs)
        context['title'] = "Ипотека"
        context['menu'] = menu

        return context

def logout_user(request):
    logout(request)
    return redirect('login')