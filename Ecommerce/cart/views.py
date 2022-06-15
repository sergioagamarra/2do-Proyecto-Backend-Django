from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CartItem, Cart
from products.models import Product
from django.utils.decorators import decorator_from_middleware
from users.middleware import AuthMiddleware
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
auth_middleware = decorator_from_middleware(AuthMiddleware)

print(auth_middleware)


@auth_middleware
def get_cart(request):
    if request.user.is_authenticated:
        products = request.user.cart.products.all()
        total = request.user.cart.total
        # for cartItem in products:
        #     total += cartItem.product.price * cartItem.amount
        return render(request, "pages/cart.html", {
            "products": products,
            "total": total
        })

    return redirect("/")


def add_to_cart(request, idProduct):
    if request.user.is_authenticated:
        cartItem = CartItem()
        cartItem.product = Product.objects.get(pk=idProduct)
        cartItem.amount = 1
        cartItem.cart = request.user.cart
        cartItem.save()

         #actualizar el total
        products = request.user.cart.products.all()
        total = 0
        for cartItem in products:
            total += cartItem.product.price * cartItem.amount

        cart = request.user.cart
        cart.total=total
        cart.save()

    return redirect("/")


@csrf_exempt
def change_amount(request):
    if request.method == "POST":
        data = json.loads(request.body)

        amount = data['amount']
        id_item = data['idItem']

        cart_item = CartItem.objects.get(id=id_item)

        cart_item.amount = amount
        cart_item.save()

        #actualizar el total
        products = request.user.cart.products.all()
        total = 0
        for cartItem in products:
            total += cartItem.product.price * cartItem.amount

        cart = request.user.cart
        cart.total=total
        cart.save()
        print(cart.total)

        return JsonResponse({
            "total": total
        })

def delete_from_cart(request, id_cart_item):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(pk=id_cart_item)
        if cart_item.cart.user == request.user:
            cart_item.delete()

            return redirect("/cart")

    return redirect("/")