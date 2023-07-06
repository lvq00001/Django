from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
