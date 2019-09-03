from django.contrib import admin
from django.urls import path
from .views import all_suggestions, single_suggestion, make_suggestion, upvote_suggestion

urlpatterns = [
    path('', all_suggestions, name='suggestions'),
    path('<int:pk>/', single_suggestion, name='single_suggestion'),
    path('make_suggestion', make_suggestion, name='make_suggestion'),
    path('upvote/<int:pk>/', upvote_suggestion, name='upvote_suggestion')
    ]