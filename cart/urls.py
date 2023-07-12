from django.urls import path
from . import views


urlpatterns = [
    path("", views.cart, name="cart"),
    path("update/<int:id>/<str:action>/", views.updateCartItem, name="updateCartItem"),
    path("delete/<int:id>", views.deleteCartItem, name="deleteCartItem"),
]
