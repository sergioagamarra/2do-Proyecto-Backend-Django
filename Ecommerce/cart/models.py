from django.db import models
from products.models import Product

# Create your models here.
class Cart(models.Model):
    pass
# Relacion 1 a 1 con user

# Create your models here.
class CartItem(models.Model):
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)