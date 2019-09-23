from django.contrib import admin
from django.urls import path
from .views import index, graphs, graph_data

urlpatterns = [
    path('', index, name="home"),
    path('graphs/', graphs, name='graphs'),
    path('graphs/graph_data/', graph_data, name='graph_data'),
    ]