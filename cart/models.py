from django.db import models
from book.models import Book
from django.contrib.auth.models import User


# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    book_quantity = models.IntegerField()

    def __str__(self):
        return self.user.username
