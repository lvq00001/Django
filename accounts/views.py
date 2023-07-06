from django.shortcuts import render
from .form import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def account(request):
    if request.method == "GET":
        return render(request, "account.html", {"form": UserCreateForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("/")
            except IntegrityError:
                return render(
                    request,
                    "account.html",
                    {
                        "form": UserCreateForm,
                        "error": "Username already taken. Choose new username.",
                    },
                )

        else:
            return render(
                request,
                "account.html",
                {"form": UserCreateForm(), "error": "Password do not match"},
            )


@login_required
def user_logout(request):
    logout(request)
    return redirect("/")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "loginaccount.html",
                {
                    "form": AuthenticationForm(),
                    "error": "username and password do not match",
                },
            )
        else:
            login(request, user)
            return redirect("/")
