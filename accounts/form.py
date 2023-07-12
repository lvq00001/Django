from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {
                    "class": "form-control w-50",
                }
            )

        self.fields["username"].label = "Tên tài khoản"
        self.fields["password1"].label = "Mật khẩu"
        self.fields["password2"].label = "Nhập lại mật khẩu"


class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)

        self.fields["username"].label = "Tên đăng nhập"
        self.fields["password"].label = "Mật khẩu"

        for fieldname in ["username", "password"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {
                    "class": "form-control w-50",
                }
            )
