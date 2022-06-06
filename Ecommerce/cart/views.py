from django.shortcuts import render

# Create your views here.
def get_cart(request):
    return render(request,"pages/cart.html")