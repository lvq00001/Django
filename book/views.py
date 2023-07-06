from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404, redirect
import locale
from cart.forms import CartItemForm

locale.setlocale(locale.LC_ALL, "")


# Create your views here.
def books(request):
    category = request.GET.get("category")
    print(category)
    if category != None:
        data = Book.objects.filter(category=category)
    else:
        data = Book.objects.all()
    return render(request, "books.html", {"books": data})


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "GET":
        book.price = locale.format_string("%.0f", int(book.price), grouping=True)
        return render(
            request, "book-detail.html", {"book": book, "form": CartItemForm()}
        )
    else:
        try:
            form = CartItemForm(request.POST)
            cartItem = form.save(commit=False)
            cartItem.user = request.user
            cartItem.book = book.title
            cartItem.book_quantity = request.POST["book_quantity"]
            cartItem.price = book.price
            cartItem.save()
            return redirect("detail", book.id)
        except ValueError:
            return render(
                request,
                "book-detail.html",
                {"form": CartItemForm(), "error": "Đã có lỗi, vui lòng thử lại"},
            )
