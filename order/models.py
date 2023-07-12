from typing import Any
from django.db import models
from django.contrib.auth.models import User
from book.models import Book


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    # def __init__(self, order, book, quantity):
    #     super().__init__(self, order, book, quantity)
    #     self.order = order
    #     self.book = book
    #     self.quantity = quantity

    def __str__(self) -> str:
        return self.book.title
