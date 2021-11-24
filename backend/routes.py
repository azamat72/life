from django.urls import path
from .views import *


urlpatterns = [
path('', index, name='index'),
path('about', about, name='about'),
path('galery', galery, name='galery'),
path('news', news, name='news'),
path('team', team, name='team'),
path('contact', contact, name='contact'),

]
