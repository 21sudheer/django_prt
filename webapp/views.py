from django.shortcuts import render, HttpResponse, redirect
from webapp.forms import webform

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import registration

from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError


# Create your views here.
def all(request):
    # return redirect("/LoginPage")
    return render(request, "all.html")


def HomePage(request):
    # return redirect("/LoginPage")
    return render(request, "home.html")


@csrf_exempt
def SignupPage(request):
    print("hi")
    form = webform()
    if request.method == "POST":
        print("hello")
        print(request.POST)

        username = request.POST.get("username")
        email = request.POST.get("email")

        password = request.POST.get("password1")
        phone_number = request.POST.get("phonenumber")

        password2 = request.POST.get("password2")

        if password != password2:
            return HttpResponse("your password and confirm password are not same!")
        else:
            print(username)
            print(email)
            print(password)
            my_user = User.objects.create_user(
                username,
                email,
                password,
            )
            my_user.save()
            return redirect("LoginPage")
        # print("middle")
        # form = webform(request.POST)

        # print(form)
        # if form.is_valid():
        #     print("enters")
        #     form.save()
        #     return HttpResponse("data inserted")

    return render(request, "signup.html")
    # if request.method == "POST":
    #     uname = request.POST.get("name")
    #     phonenumber = request.POST.get("phonenumber")
    #     email = request.POST.get("email")
    #     pass1 = request.POST.get("password1")
    #     pass2 = request.POST.get("password2")

    #     if pass1 != pass2:
    #         return HttpResponse("your password and confirm password are not same!")
    #     else:
    #         print(uname)
    #         print(email)
    #         print(pass1)
    #         my_user = User.objects.create_user(
    #             email,
    #             pass1,
    #         )
    #         my_user.save()
    #         return redirect("LoginPage")
    # return render(request, "signup.html")
    # return HttpResponse("user has been created successfully")
    # print(uname, phonenumber, emailid, pass1, pass2)


@csrf_exempt
def LoginPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(request.POST)
        Emp = authenticate(
            username=username,
            password=password,
        )
        print(Emp)
        if Emp:
            return redirect("/HomePage")
        return redirect("/SignupPage")

    # return redirect("/HomePage")
    return render(request, template_name="login.html")


def logoutPage(request):
    logout(request)
    return redirect("/LoginPage")
    # return render(request, "login.html")


# Create your views here.
def forgotpassword(request):
    return render(request, "forgot_password.html")


def Recoverpassword(request):
    return redirect("/LoginPage")
    # return render(request, "recover_password.html")
