from django.shortcuts import render

from apps.users.models import User


def login(request, *args, **kwargs):

    if request.method == "POST":
        pass

    return render(request, "login.html")


def logout(request, *args, **kwargs):

    return render(request, "logout.html")
