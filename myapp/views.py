from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.forms import UserForm, ExtendedUserForm, UserSigninForm
#
from myapp.models import Location
from myapp.services.flick_api import FlickrData
from myapp.services.service import LocationService, FavouriteImageService


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
            return to home page if login success
             else return to signin page
    """
    # user_signin_form = UserSigninForm()
    # return render(request, "myapp/signupsignin.html",
    # ==================================
    if request.method == "POST":
        # user_signin_form = UserSigninForm(request.POST)
        # print("user_signin_form : ", user_signin_form)
        username = request.POST['username']
        password = request.POST['password']
        print("*************************************************************")
        print("username ", username)
        print("password ", password)
        # print("user_signin_form.is_valid()", user_signin_form.is_valid())
        # if user_signin_form.is_valid():
        # ===================authenticate predefined======================
        user = authenticate(username=username, password=password)
        # user = authenticate(request, username=username, password=password,)
        print("user : ", user)
        if user is not None:
            login(request, user)
            # return render(request, "myapp/home")
            # html = render_to_string('myapp/home.html')
            # return Response({"status": 200, "message": "Success"})
            return redirect("home")
        else:
            # return Response({"status": 0, "message": "Failed"})
            return redirect('signin')
        # ===================coustom======================
        # try:
        #     user = User.objects.get(username=username)
        #     print("user : ", user)
        #     print("user : ", user.username)
        #     print("user : ", user.password)
        #     if username == user.username and password == user.password:
        #         name = user.first_name + " " + user.last_name
        #         print(name)
        #         username = user.username
        #         print(username)
        #         # return Response({"status": 200, "message": "Success"})
        #         # return render(request, "myapp/home.html",
        #         #               {"name": name})
        #         return redirect("home")
        #     else:
        #         print("your are in else")
        #         # return Response({"status": 0, "message": "Failed"})
        #         messages.error(request, "Bad Credentials!!")
        #         return redirect('signin')
        # except User.DoesNotExist:
        #     print("your are in except")
        #
        #     # return Response({"status": 0, "message": "Failed"})
        #     messages.error(request, "Bad Credentials!!")
        #     return redirect('signin')

    # ==================================
    else:
        user_signin_form = UserSigninForm()
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


# @api_view(["POST"])
# def log_in(request):
#     if request.method == "POST":
#         # user_signin_form = UserSigninForm(request.POST)
#         # print("user_signin_form : ", user_signin_form)
#         username = request.POST['username']
#         password = request.POST['password']
#         print("*************************************************************")
#         print("username ", username)
#         print("password ", password)
#         # print("user_signin_form.is_valid()", user_signin_form.is_valid())
#         # if user_signin_form.is_valid():
#         # ===================authenticate predefined======================
#         user = authenticate(username=username, password=password)
#         # user = authenticate(request, username=username, password=password,)
#         print("user : ", user)
#         if user is not None:
#             login(request, user)
#             # return render(request, "myapp/home")
#             # html = render_to_string('myapp/home.html')
#             # return Response({"status": 200, "message": "Success"})
#             return redirect("home")
#         else:
#             # return Response({"status": 0, "message": "Failed"})
#             return redirect('signin')
#         # ===================coustom======================
#         # try:
#         #     user = User.objects.get(username=username)
#         #     print("user : ", user)
#         #     print("user : ", user.username)
#         #     print("user : ", user.password)
#         #     if username == user.username and password == user.password:
#         #         name = user.first_name + " " + user.last_name
#         #         print(name)
#         #         # return Response({"status": 200, "message": "Success"})
#         #         return redirect("home")
#         #     else:
#         #         print("your are in else")
#         #         # return Response({"status": 0, "message": "Failed"})
#         #         messages.error(request, "Bad Credentials!!")
#         #         return redirect('signin')
#         # except User.DoesNotExist:
#         #     print("your are in except")
#         #
#         #     # return Response({"status": 0, "message": "Failed"})
#         #     messages.error(request, "Bad Credentials!!")
#         #     return redirect('signin')
#

def home(request):
    # name = "Prakash"
    print("you are in home")
    # print("request.user", request.user)
    name = request.user
    # print("name", name)
    # return render(request, "myapp/home.html")
    return render(request, "myapp/home.html", {"name": name})


class LocationList(APIView):
    """
           Return Location list present in database with given term

            method type : get
            Param : term
            Return : [location name]
            Rtype : Response

    """

    def get(self, request, name):
        search_term = name
        print("search_term : ", search_term)
        location_names = list(Location.objects.filter(name__icontains=search_term).values_list("name", flat=True))
        return Response(location_names)


class InsertLocation(APIView):
    """
           Insert given Location

            method type : post
            Param : location_name
            Return : status
            Rtype : Response

    """

    def post(self, request):
        # serializer_data = LocationSerializer(data=request.data)
        # if serializer_data.is_valid():
        #     name = serializer_data.data["name"]
        #     location_service = LocationService()
        #     response = location_service.insert_location(name)
        #     return Response({"status": 200, "name": response})
        name = request.data["location_name"]
        print("new name : ", name)
        location_service = LocationService()
        response = location_service.insert_location(name)
        return Response({"status": 200, "name": response})


class LikeUnlike(APIView):
    """
           Return response status for like and unlike

            method type : post
            Param : image_url
            Return : status
            Rtype : Response

    """

    def post(self, request):
        image_url = request.data["image_url"]
        # print("new image_url : ", image_url)
        # user = request.user
        # print("User : ", user)
        # user_object = User.objects.filter(username__iexact=user)
        # print("user_object :", user_object)
        user_id = request.data["user_id"]
        # print("new user_id  : ", user_id)
        fav_image_service = FavouriteImageService()
        response = fav_image_service.insert_delete_image(user_id, image_url)
        # print("return response : ", response)
        # print("return response : ", response.status_code)
        return Response({"status": response.status_code})


class FavouriteImages(APIView):
    """
            Return Favourite images for given user

            Param : user_id
            Return : Image_url List
            Rtype : Response
     """

    def get(self, request, user_id):
        favourite_service = FavouriteImageService()
        favourite_images = favourite_service.get_favourites(user_id)
        return Response(favourite_images)


class SearchImages(APIView):
    """
           Return search Images by location name with page ,if page number given
           otherwise page number 1

            method type : get
            Param : location_name, page_number
            Return : images, page, total_pages, favourite_images
            Rtype : json responseFavouriteImageService

    """

    def get(self, request):
        # user_id = request.session.get('id')
        # print("user_id", user_id)
        location_name = request.data['location_name']
        page_number = request.data['page_number']
        print(location_name, page_number)
        print("***************************************")
        print(request.data['location_name'] is None)
        flickr_service = FlickrData()
        image_data, page, total_pages = flickr_service.searchImageData(page_number, location_name)

        return Response({"imageData": image_data, "page": page, "total_pages": total_pages})


def signout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect("signin")
