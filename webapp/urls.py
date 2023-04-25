from django.urls import path
from . import views

urlpatterns = [
    path("", views.all, name="all"),
    path("HomePage", views.HomePage, name="HomePage"),
    path("SignupPage", views.SignupPage, name="SignupPage"),
    path("LoginPage", views.LoginPage, name="LoginPage"),
    path("logoutPage", views.logoutPage, name="logoutPage"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("Recoverpassword", views.Recoverpassword, name="Recoverpassword"),
]
