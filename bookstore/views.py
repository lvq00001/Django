from django.shortcuts import render
from book.models import Book
from django.db.models import FloatField
from django.db.models.functions import Cast
import locale
from django.core.paginator import Paginator, EmptyPage


def home(request):
    searchTerm = request.GET.get("searchBook")
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()

    priceOrder = request.GET.get("priceOrder")
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
        next = books.next_page_number() if books.has_next() else 4
        pre = books.previous_page_number() if books.has_previous() else 1
    except EmptyPage:
        pass

    return render(
        request,
        "home.html",
        {
            "searchTerm": searchTerm,
            "books": books,
            "page": page,
            "next": next,
            "pre": pre,
        },
    )
