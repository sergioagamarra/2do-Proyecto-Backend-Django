from django.shortcuts import render
from .models import Product
from .models import Category

# Create your views here.
def home(request):
    #print(request.user.cart.products.all())
    products = Product.objects.all()
    #products = Product.objects.filter(categories=1)
    #products = Category.objects.get(pk=1).products.all()
    print(products)
    return render(request, "pages/home.html",{
        "products": products
    })