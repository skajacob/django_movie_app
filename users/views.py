"""Users app views"""

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import SignupForm


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect("movies:list")
        else:
            context["error"] = "Credenciales incorrectas"
    return render(request, "users/login.html", context)


def user_signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("movies:list")
    return render(request, "users/signup.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("users:login")