from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart, name="cart"),
    path('add/<int:idProduct>', views.add_to_cart, name="add_to_cart"),
    path('change_amount', views.change_amount, name="change_amount"),
    path('delete/<int:id_cart_item>', views.delete_from_cart, name="delete_from_cart")
]