
from django.urls import path, include
from ProfileApp import views

urlpatterns = [
    path('base', views.base, name='base'),
    path('Menu', views.Menu, name='Menu'),
    path('Home', views.Home, name='Home'),
    path('Header', views.Header, name='Header'),
    path('Profile', views.Profile, name='Profile'),
    path('Education', views.Education, name='Education'),
    path('interests', views.interests, name='interests'),
    path('Sale', views.Sale, name='Sale'),
    path('Idol', views.Idol, name='Idol'),
    path('Contact', views.Contact, name='Contact'),

]
