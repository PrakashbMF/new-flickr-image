from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from myapp.forms import UserForm, ExtendedUserForm, UserSigninForm


#
def signup(request):
    """
           Render to Signup page
    """
    user_form = UserForm()
    extended_user_form = ExtendedUserForm()
    # return render(request, "myapp/signupsignin.html",
    return render(request, "myapp/signup.html",
                  {"user_form": user_form, "extended_user_form": extended_user_form})


def signin(request):
    """
           Render to Signup page
    """
    user_signin_form = UserSigninForm()
    # return render(request, "myapp/signupsignin.html",
    return render(request, "myapp/signin.html",
                  {"user_signin_form": user_signin_form})


@api_view(['POST'])
def create_user(request):
    """
           Account will create successfully if every data valid to Signup and response as successful
           else error response will display
    """
    if request.method == 'POST':
        print("request user : ", request.user)
        user_form = UserForm(request.POST)
        extended_user_form = ExtendedUserForm(request.POST)
        # print("user_form :", user_form)
        # print("extended_user_form :", extended_user_form)
        if user_form.is_valid() and extended_user_form.is_valid():
            user = user_form.save()
            extended_user = extended_user_form.save(commit=False)
            extended_user.user = user
            extended_user.save()
            # extended_user_form.save(user=user)
            return Response({"message": "Account has created successfully"})
        else:
            return Response({"message": "Please Enter valid Information"})


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def log_in(request):
    if request.method == "POST":
        # user_signin_form = UserSigninForm(request.POST)
        # print("user_signin_form : ", user_signin_form)
        username = request.POST['username']
        password = request.POST['password']
        print("************************************************************* ")
        print("username ", username)
        print("password ", password)
        # print("user_signin_form.is_valid()", user_signin_form.is_valid())
        # if user_signin_form.is_valid():
        # ===================authenticate predefined======================
        # user = authenticate(request, username=username, password=password)
        # print("user : ", user)
        # if user is not None:
        #     login(request, user)
        #     # return render(request, "myapp/home")
        #     # html = render_to_string('myapp/home.html')
        #     return Response({"status": 200, "message": "Success"})
        #
        # else:
        #     return Response({"status": 0, "message": "Failed"})
        # ===================coustom======================
        try:
            user = User.objects.get(username=username)
            print("user : ", user)
            print("user : ", user.username)
            print("user : ", user.password)
            if username == user.username and password == user.password:
                name = user.first_name + " " + user.last_name
                print(name)
                # return Response({"status": 200, "message": "Success"})
                return redirect("home")
            else:
                print("your are in else")
                # return Response({"status": 0, "message": "Failed"})
                messages.error(request, "Bad Credentials!!")
                return redirect('signin')
        except User.DoesNotExist:
            print("your are in except")

            # return Response({"status": 0, "message": "Failed"})
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')


def home(request):
    name = "Prakash"
    return render(request, "myapp/home.html", {"name": name})


def log_out(request):
    logout(request)
    return render(request, 'myapp/signin.html')
