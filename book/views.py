from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404, redirect
import locale
from cart.forms import CartItemForm
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.core.paginator import Paginator, EmptyPage

locale.setlocale(locale.LC_ALL, "")


# Create your views here.
def books(request):
    category = request.GET.get("category")
    if category != None:
        books = Book.objects.filter(category=category)
    else:
        books = Book.objects.all()

    page = request.GET.get("page")
    if page == None:
        page = 1
    try:
        paginator = Paginator(books, 6)
        books = paginator.get_page(page)
        total_page = paginator.num_pages
    except EmptyPage:
        pass

    return render(
        request,
        "books.html",
        {
            "books": books,
            "page": page,
            "total_page": total_page,
        },
    )


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "GET":
        # book.price = locale.format_string("%.0f", int(book.price), grouping=True)
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
            success = "Đã thêm vào giỏ hàng."
            return render(
                request,
                "book-detail.html",
                {"form": CartItemForm(), "book": book, "success": success},
            )
        except ValueError:
            return render(
                request,
                "book-detail.html",
                {"form": CartItemForm(), "error": "Đã có lỗi, vui lòng thử lại"},
            )


def priceOrder(request):
    books = Book.objects.all()
    priceOrder = request.GET.get("order")
    if priceOrder == "asc":
        books = books.annotate(
            num_price=Cast("price", output_field=FloatField()),
        ).order_by("num_price")
    else:
        books = books.annotate(
            num_price=Cast("price", output_field=FloatField()),
        ).order_by("-num_price")

    page = request.GET.get("page")
    if page == None:
        page = 1
    try:
        paginator = Paginator(books, 6)
        books = paginator.get_page(page)
        total_page = paginator.num_pages
    except EmptyPage:
        pass

    return render(
        request,
        "books.html",
        {
            "books": books,
            "page": page,
            "total_page": total_page,
        },
    )


def titleOrder(request):
    books = Book.objects.all()
    titleOrder = request.GET.get("title")
    if titleOrder == "asc":
        books = books.order_by("title")
    else:
        books = books.order_by("-title")

    page = request.GET.get("page")
    if page == None:
        page = 1
    try:
        paginator = Paginator(books, 6)
        books = paginator.get_page(page)
        total_page = paginator.num_pages
    except EmptyPage:
        pass

    return render(
        request,
        "books.html",
        {
            "books": books,
            "page": page,
            "total_page": total_page,
        },
    )
