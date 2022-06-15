from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("perfil/", views.perfil_view, name="perfil"),
    path("edit/", views.edit_view, name="edit"),
    path("verify/<str:email_uuid>", views.validate_email, name="email_validation")
]