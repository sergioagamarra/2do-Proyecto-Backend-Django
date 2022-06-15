from django.shortcuts import render, redirect


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return self.get_response(request)

        return redirect("/")
