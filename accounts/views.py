from django.shortcuts import render
from .form import UserCreateForm, UserAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
import re

# Create your views here.


def account(request):
    if request.method == "GET":
        return render(request, "account.html", {"form": UserCreateForm})
    else:
        try:
            if re.match("^[a-zA-Z0-9]+$", request.POST["username"]) is None:
                raise Exception
            if request.POST["password1"] == request.POST["password2"]:
                if (
                    password_validation.validate_password(request.POST["password1"])
                    is not None
                ):
                    raise ValidationError
                else:
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
                                "error": "Tên tài khoản đã tồn tại. Chọn tên tài khoản khác.",
                            },
                        )
        except ValidationError:
            return render(
                request,
                "account.html",
                {
                    "form": UserCreateForm,
                    "error": "Mật khẩu ít nhất 6 kí tự, bao gồm chữ và số.",
                },
            )
        except Exception:
            return render(
                request,
                "account.html",
                {
                    "form": UserCreateForm,
                    "error": "Tên tài khoản không được chứa kí tự đặc biệt.",
                },
            )

        else:
            return render(
                request,
                "account.html",
                {"form": UserCreateForm(), "error": "Mật khẩu không trùng khớp."},
            )


@login_required
def user_logout(request):
    logout(request)
    return redirect("/")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": UserAuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": UserAuthenticationForm(),
                    "error": "Tên đăng nhập hoặc mật khẩu không đúng.",
                },
            )
        else:
            login(request, user)
            return redirect("/")
