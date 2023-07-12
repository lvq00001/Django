from django.shortcuts import render
from cart.models import CartItem
from order.models import Order, OrderItem
from book.models import Book
from cart.models import CartItem
from .forms import OrderForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def order(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "order.html", {"orders": orders})


@login_required
def createOrder(request):
    checkbox = list(request.GET.keys())
    print(checkbox)
    if len(checkbox) == 0:
        error = "Chọn sản phẩm trước khi nhấn mua hàng."
        cart = CartItem.objects.filter(user=request.user)
        total = 0
        for item in cart:
            total += int(item.price) * int(item.book_quantity)
        return render(
            request, "cart.html", {"cart": cart, "total": total, "error": error}
        )

    cart = CartItem.objects.filter(id__in=checkbox)
    total = 0
    for c in cart:
        total += int(c.price) * int(c.book_quantity)
    if request.method == "GET":
        return render(
            request,
            "create-order.html",
            {"form": OrderForm, "cart": cart, "total": total},
        )
    else:
        try:
            form = OrderForm(request.POST)
            newOrder = form.save(commit=False)
            newOrder.user = request.user
            newOrder.address = request.POST["address"]
            newOrder.phone = request.POST["phone"]
            newOrder.total = total
            newOrder.save()

            for c in cart:
                newOrderItem = OrderItem(
                    order=newOrder,
                    book=Book.objects.get(title=c.book),
                    quantity=c.book_quantity,
                )
                newOrderItem.save()
                cartItem = CartItem.objects.get(book=c.book)
                cartItem.delete()

            return redirect("order")
        except ValueError:
            return render(
                request,
                "create-order.html",
                {"form": OrderForm(), "error": "Đã có lỗi vui lòng thử lại."},
            )
