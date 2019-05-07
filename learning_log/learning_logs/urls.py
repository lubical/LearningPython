"""Defines URL patterns for learning_logs.
   update information: https://ehmatthes.github.io/pcc/chapter_18/README.html#updates
"""
from django.urls import path
from . import views
app_name='learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
