from django.shortcuts import render

# Create your views here.
from myapp.forms import UserForm, ExtendedUserForm


#
def signup(request):
    """
           Render to platform page
    """
    user_form = UserForm()
    extended_user_form = ExtendedUserForm()
    # return render(request, "myapp/signupsignin.html",
    return render(request, "myapp/signup.html",
                  {"user_form": user_form, "extended_user_form": extended_user_form})


# def signup(request):
#     """
#            Render to platform page
#
#     """
#     return render(request, "myapp/signup.html")
