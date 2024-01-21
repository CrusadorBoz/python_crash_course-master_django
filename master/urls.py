""" Defines URL patterns for master. """

from django.urls import path

from . import views

app_name = 'master'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    path('pizza', views.pizza, name='pizza'),

    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

]
