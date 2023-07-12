from django.forms import ModelForm, NumberInput
from .models import CartItem


class CartItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["book_quantity"].widget.attrs.update({"class": "col-md-1"})
        self.fields["book_quantity"].initial = 1

    class Meta:
        model = CartItem
        fields = ["book_quantity"]
        widgets = {"book_quantity": NumberInput}
        labels = {"book_quantity": ("Số lượng")}
