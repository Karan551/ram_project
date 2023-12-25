from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.handleLogin, name="login"),
    path("signup/", views.handleSignUp, name="signup"),
    path("pricing/", views.feature, name="feature"),
    path("payment/", views.paymentMethod, name="payment"),

]
