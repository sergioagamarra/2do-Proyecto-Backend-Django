from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    image = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, related_name="categories")

    def __str__(self):
        return self.name