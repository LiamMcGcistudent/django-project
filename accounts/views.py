from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from .forms import UserLoginForm, UserRegistrationForm
from reviews.models import Review
from django.db.models import Count


def registration(request):
    """
    Renders a page with a registration form
    so users can sign up for the site
    """
    if request.user.is_authenticated:
        return redirect(reverse('login'))

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            messages.success(request, f"Account created for {username}.")
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def user_profile(request):
    """
    Profile page for the logged in user.
    """
    
    user = User.objects.get(username=request.user.username)
    
    return render(request, "profile.html", {"profile": user})


def login(request):
    """
    Creates a view to allow users to login
    """
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your username or password is incorrect")
    else:
        form = UserLoginForm
    return render(request, 'login.html', {'form': form})


@login_required()
def logout(request):
    """
    Allows a user to logout
    """
    auth.logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect(reverse('home'))
    
    