from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields["address"].widget.attrs.update(
            {"class": "form-control border-primary"}
        )
        self.fields["phone"].widget.attrs.update(
            {"class": "form-control border-primary"}
        )

    class Meta:
        model = Order
        fields = ["address", "phone"]
        labels = {"address": ("Địa chỉ"), "phone": ("Số điện thoại")}
