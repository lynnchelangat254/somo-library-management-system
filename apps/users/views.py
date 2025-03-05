from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from apps.users.forms import LoginForm, MemberRequestForm


def login_user(request, *args, **kwargs):

    if request.method == "POST":
        form = LoginForm(request.POST)
        next_url = request.GET.get("next")
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)

            # check if user exists and user is a librarian
            if user and user.role == "Librarian":
                messages.success(request, "User logged in successfully!")
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return redirect("librarian-dashboard")
            # check if user exists and user is a member
            elif user and user.role == "member":
                messages.success(request, "User logged in successfully!")
                login(request, user)
                if next_url:
                    return redirect(next_url)
                return redirect("member-dashboard")
            else:
                messages.error(request, "User authentication failed!")
                return render(request, "login.html", {"form": form})
    form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_user(request, *args, **kwargs):
    """Log out"""
    logout(request)
    messages.success(request, "User logged out successfully!")
    return redirect("home")


def membership(request, *args, **kwargs):
    """Membership Request Form"""
    if request.method == "POST":
        form = MemberRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = MemberRequestForm()
    return render(request, "membership.html", {"form": form})
