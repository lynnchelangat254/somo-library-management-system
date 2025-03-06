from django.contrib import admin
from django.urls import path, include

from apps.users.views import login_user, logout_user, membership

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("membership/", membership, name="membership"),
]
