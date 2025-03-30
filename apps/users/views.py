from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from apps.users.forms import LoginForm, MemberRequestForm
from apps.users.models import User
from apps.members.models import Member


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
            elif user and user.role == "Member":
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
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            # check if passwords match
            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect("membership")

            # check if user already exists
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                messages.error(request, "User with this email already exists!")
                return redirect("membership")

            # create a new user with the provided data
            user = User(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                country=form.cleaned_data["country"],
                city=form.cleaned_data["city"],
                gender=form.cleaned_data["gender"],
            )
            user.set_password(password)
            user.save()

            # create a new member record for the created user
            member = Member(user=user)
            member.save()
            messages.success(
                request,
                "Membership request sent successfully, kindly be patient as a librarian confirms your membership!",
            )
            return redirect("membership")

        messages.error(request, "Membership request failed, please try again!")
        return redirect("membership")
    form = MemberRequestForm()
    return render(request, "membership.html", {"form": form})


def reset_password(request, *args, **kwargs):
    """Reset Password Form"""
    # TODO: Implement password reset functionality here
    pass

def update_profile(request, *args, **kwargs):
    # TODO: Implement profile update functionality here
    pass

def contact_us(request, *args, **kwargs):
    # TODO: Implement contact us functionality here
    pass

def faq(request, *args, **kwargs):
    # TODO: Implement FAQ functionality here
    pass

def about_us(request, *args, **kwargs):
    # TODO: Implement about us functionality here
    pass
