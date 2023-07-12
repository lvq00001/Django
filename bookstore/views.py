from django.shortcuts import render
from book.models import Book

from django.core.paginator import Paginator, EmptyPage


def home(request):
    slider = [
        "https://i.imgur.com/HfOfBPL.jpg",
        "https://i.imgur.com/MyYBk4q.jpg",
        "https://i.imgur.com/kNTR97B.jpg",
    ]
    searchTerm = request.GET.get("searchBook")
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()

    page = request.GET.get("page")
    if page == None:
        page = 1
    try:
        paginator = Paginator(books, 6)
        books = paginator.get_page(page)
        total_page = paginator.num_pages
        # next = books.next_page_number() if books.has_next() else 4
        # pre = books.previous_page_number() if books.has_previous() else 1
    except EmptyPage:
        pass

    return render(
        request,
        "home.html",
        {
            "searchTerm": searchTerm,
            "books": books,
            "slider": slider,
            "page": page,
            "total_page": total_page,
        },
    )
