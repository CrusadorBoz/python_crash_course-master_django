""" Defines URL patterns for master. """

from django.urls import path

from . import views

app_name = 'master'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    
]
