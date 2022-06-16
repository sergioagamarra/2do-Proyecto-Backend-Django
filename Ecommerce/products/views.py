from django.shortcuts import render
from .models import Product
from .models import Category

# Create your views here.
def home(request):
    #print(request.user.cart.products.all())
    products = Product.objects.all()
    #products = Product.objects.filter(categories=1)
    #products = Category.objects.get(pk=1).products.all()
    #print(products)
    categories = Category.objects.all()
    return render(request, "pages/home.html",{
        "products": products,
        "categories": categories
    })
    
def search_product(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Product.objects.filter(name__icontains = search)
        categories = Category.objects.all()
    
    return render(request, "pages/home.html",{
        "products": products,
        "categories": categories
    })
    
def filter_by_category(request, idCategory):
    products = Product.objects.filter(categories=idCategory)
    categories = Category.objects.all()
    return render(request, "pages/home.html",{
        "products": products,
        "categories": categories
    })
    
def filter_by_price(request, asc):
    if asc == 1:
        products = Product.objects.all().order_by("price")
    else: 
        products = Product.objects.all().order_by("-price")
    categories = Category.objects.all()
    return render(request, "pages/home.html",{
        "products": products,
        "categories": categories
    })