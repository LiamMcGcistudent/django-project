from django.contrib import admin
from django.urls import path
from .views import view_cart, add, adjust

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('<int:id>/add/', add, name="add"),
    path('<int:id>/adjust/', adjust, name="adjust")
]