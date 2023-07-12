from django.urls import path
from . import views

urlpatterns = [
    path("", views.books, name="books"),
    path("<int:book_id>", views.detail, name="detail"),
    path("price", views.priceOrder, name="priceOrder"),
    path("title", views.titleOrder, name="titleOrder"),
]
