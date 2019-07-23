from django.contrib import admin
from django.urls import path
from .views import login, logout, user_profile, registration


urlpatterns = [
    path('', login, name="login"),
    path('registration/', registration, name="registration"),
    path('logout/', logout, name="logout"),
    path('profile/', user_profile, name="profile"),
]