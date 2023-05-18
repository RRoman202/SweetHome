from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', SweetHome.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('news/<slug:news_slug>/', ShowNews.as_view(), name='news'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('newbuildings/', NewBuildingKatalog.as_view(), name='newbuilding'),
    path('person/', PersonView.as_view(), name='person'),
    path('rent/', RentView.as_view(), name='rent'),

]