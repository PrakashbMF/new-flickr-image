from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http.request import QueryDict
from django.shortcuts import redirect
# Create your views here.
from django.utils import timezone
from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.forms import UserForm, UserSigninForm
#
from myapp.models import Location, Favourite, User
from myapp.util.flick_api import FlickrData
from myapp.util.service import GeoLocation


class Signup(TemplateView):
    """
           Render to Signup page
    """
    template_name = "myapp/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_form = UserForm()
        context['user_form'] = user_form
        return context


class Signin(TemplateView):
    """
            return to home page if login success
             else return to signin page
    """
    template_name = "myapp/signin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_signin_form = UserSigninForm()
        context['user_signin_form'] = user_signin_form
        return context

    # ==================================
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Bad Credentials !!")
            return redirect('signin')


class CreateUser(APIView):
    """
           Account will create successfully if every data valid to Signup and response as successful
           else error response will display
    """

    def post(self, request, *args, **kwargs):
        password = request.data["password"]
        if isinstance(request.data, QueryDict):  # optional
            request.data._mutable = True
            request.data.update({"password": make_password(password=password)})

        user_form = UserForm(request.POST)
        if user_form.is_valid():
            try:
                print("user_form", user_form)
                user_form.save()
                UserForm()
                return Response({"message": "Account has created successfully"})
            except Exception:
                return Response(Exception)
        else:
            UserForm()
            print("user_form.errors : ", user_form.errors)
            return Response({"message": "Please Enter valid Email Information"})


class Home(TemplateView):
    """
           Redirect to requested user Home page after login success

    """
    template_name = "myapp/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.user.first_name
        user_id = self.request.user.id
        context['name'] = name
        context['user_id'] = user_id
        return context


class FavouriteImage(TemplateView):
    """
              Redirect to requested user favourite page and show liked images if any
              else show a message
       """
    template_name = "myapp/favourite.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.user.first_name
        user_id = self.request.user.id
        context['name'] = name
        context['user_id'] = user_id
        return context


class GetFavouriteImages(APIView):
    """
              Redirect to requested user favourite page and show liked images if any
              else show a message
       """

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get("user_id")
        user = User.objects.get(id=user_id)
        favourite_images = list(
            user.favourite_set.all().order_by("-genDate").values_list("image_url", flat=True))
        return Response({"favourite_images": favourite_images}, status=status.HTTP_200_OK)


class LocationList(APIView):
    """
           Return Location list present in database with given term

            method type : get
            Param : term
            Return : [location name]
            Rtype : Response

    """

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get("term")
        location_names = list(Location.objects.filter(name__contains=search_term).values_list("name", flat=True))
        print(location_names)
        return Response(location_names, status=status.HTTP_200_OK)


class InsertLocation(APIView):
    """
           Insert given Location

            method type : post
            Param : location_name
            Return : status
            Rtype : Response
    """

    def post(self, request):
        name = request.data["location_name"]
        print("new name : ", name)
        object_data, status_data = Location.objects.get_or_create(
            name=name,
            defaults={"genDate": timezone.now(), }
        )
        return Response(status.HTTP_200_OK)


class GeoLocationFromLatLong(APIView):
    """
           Return location name by longitude and latitude and if location present in db then return that location name
           else insert in db

            method type : get
            Param : latitude, longitude
            Return : location_name
            Rtype : json response

    """

    def get(self, request, *args, **kwargs):
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")

        geo_location_service = GeoLocation()
        location_name = geo_location_service.get_geo_location(latitude, longitude)

        searched_item = list(Location.objects.filter(name=location_name).values_list("name", flat=True))
        if not searched_item:
            Location.objects.create(name=location_name, genDate=timezone.now())
        return Response({"location_name": location_name}, status=status.HTTP_200_OK)


class LikeUnlike(APIView):
    """
           Return response status for like and unlike
           if image url is present in db for request user then it will delete
           else insert that url for requested user

            method type : post
            Param : image_url
            Return : status
            Rtype : Response

    """

    def post(self, request, *args, **kwargs):
        image_url = request.data["image_url"]
        user_id = request.data["user_id"]
        object_data, status_data = Favourite.objects.get_or_create(
            image_url=image_url,
            user_id=user_id,
            defaults={"genDate": timezone.now(), }
        )
        if status_data is False:
            object_data.delete()
        return Response(status.HTTP_200_OK)


class GetLocationByParamAndInsert(APIView):
    """
               Return searched input list  if input is present in db
               otherwise it will insert that input in db and return that input

                method type : get
                Param : term
                Return : images, page, total_pages, favourite_images

        """

    def get(self, request, *args, **kwargs):
        search_term = request.query_params.get("term")
        searched_items = list(Location.objects.filter(name__contains=search_term).values_list("name", flat=True))
        if searched_items:
            return Response(searched_items, status=status.HTTP_200_OK)
        else:
            Location.objects.create(name=search_term, genDate=timezone.now())
            searched_items.append(search_term)
            return Response(searched_items, status=status.HTTP_200_OK)


class SearchImages(APIView):
    """
           Return search Images by location name with page ,if page number given
           otherwise page number 1

            method type : get
            Param : location_name, page_number
            Return : images, page, total_pages, favourite_images
            Rtype : json response

    """

    def post(self, request, *args, **kwargs):

        user_id = request.data["user_id"]
        if request.data['location_name'] == "":
            location_name = None
        else:
            location_name = request.data['location_name']
        page_number = request.data['page_number']
        flickr_service = FlickrData()
        image_data, page, total_pages = flickr_service.searchImageData(page_number, location_name)
        user = User.objects.get(id=user_id)
        favourite_images = list(
            user.favourite_set.all().order_by("-genDate").values_list("image_url", flat=True))
        for x in image_data:
            if x[0] in favourite_images:
                x.append(True)
            else:
                x.append(False)

        return Response(
            {"imageData": image_data, "page": page, "total_pages": total_pages}, status=status.HTTP_200_OK)


class SignOut(TemplateView):
    """
        Logout the request and redirect to login page
    """
    template_name = "myapp/signin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logout(self.request)
        messages.success(self.request, "Logout Success")
        user_signin_form = UserSigninForm()
        context['user_signin_form'] = user_signin_form
        return context
