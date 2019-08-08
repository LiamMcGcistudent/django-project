from django.contrib import admin
from django.urls import path
from .views import get_reviews, full_review, create_or_edit_review

urlpatterns = [
    path('', get_reviews, name='reviews'),
    path('<int:pk>/', full_review, name='full_review'),
    path('new_review/', create_or_edit_review, name='new_review'),
    path('<int:pk>/edit/', create_or_edit_review, name='edit_review')
    ]