from django.shortcuts import render
from .models import CartItem, Book
from django.shortcuts import get_object_or_404, redirect
from .forms import CartItemForm

# Create your views here.


def cart(request):
    cart = CartItem.objects.filter(user=request.user)
    total = 0
    for item in cart:
        total += int(item.price) * int(item.book_quantity)
    return render(request, "cart.html", {"cart": cart, "total": total})


# def createCartItem(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     return render(request, "book-detail.html", {"book": book, "form": CartItemForm()})


def updateCartItem(request, id, action):
    cartItem = CartItem.objects.get(id=id)
    if action == "plus":
        cartItem.book_quantity += 1
    else:
        if cartItem.book_quantity > 1:
            cartItem.book_quantity -= 1
        else:
            pass
    cartItem.save()
    return redirect("/cart")


def deleteCartItem(request, id):
    cartItem = CartItem.objects.get(id=id)
    cartItem.delete()
    return redirect("/cart")
