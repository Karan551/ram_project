from django.shortcuts import render
# from .models import Register
from .utils import registerUser, loginUser


# Create your views here.
def index(request):
    return render(request, "fitness/index.html")


def feature(request):
    return render(request, "fitness/feature.html")


def pricing(request):
    return render(request, "fitness/price.html")


def handleLogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["user-password"]
        user_details = {
            "email": email,
            "password": password
        }
        response = loginUser(user_details)
        if response["statusCode"] == 200:
            return render(request, "fitness/private.html", {"msg": response["msg"], "status": True})
        elif response["statusCode"] == 503 and response["msg"] == "Password Incorrect.":
            return render(request, "fitness/login.html", {"msg": response["msg"], "status": False})
        else:
            return render(request, "fitness/login.html", {"msg": response["msg"], "status": False})

    return render(request, "fitness/login.html")


def handleSignUp(request):
    if request.method == "POST":
        firstName = request.POST["first-name"]
        lastName = request.POST["last-name"]
        contact = request.POST["contact"]
        email = request.POST["email"]
        address = request.POST["address-line-1"] + " " + request.POST["address-line-2"]
        password = request.POST["password"]
        fullName = firstName + " " + lastName
        # Create User Data dict.
        user_details = {
            "name": fullName,
            "contact": contact,
            "email": email,
            "address": address,
            "password": password
        }
        response = registerUser(user_details)
        if response["statusCode"] == 200:
            return render(request, "fitness/signup.html", {"msg": response['msg']})
        else:
            return render(request, "fitness/signup.html", {"msg": response['msg']})
    return render(request, "fitness/signup.html")


def paymentMethod(request):
    return render(request, "fitness/pay.html")
