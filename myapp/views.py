from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
        """
            send context to html page
        """
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
        """
            send context to html page
        """
        context = super().get_context_data(**kwargs)
        user_signin_form = UserSigninForm()
        context['user_signin_form'] = user_signin_form
        return context

    # ==================================
    def post(self, request, *args, **kwargs):
        """
            On correct email and password render to home page
             else return to signin page
        """
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
           This will create user
           else error response will display
    """

    def post(self, request, *args, **kwargs):
        """
            Account will create successfully if every data valid to Signup and response as successful
            else error response will display

            method type : post
            Rtype : Response
        """
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        password = request.data["password"]
        phone = request.data["phone"]
        age = request.data["age"]
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            try:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                                age=age)
                user.set_password(password)
                user.save()
                return Response({"message": "Account has created successfully"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"message": "Please Enter valid Email Information"})


class Home(TemplateView):
    """
           Redirect to requested user Home page after login success

    """
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        """
            send context to home html page
        """
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

    def get_context_data(self, **kwargs):
        """
            send context to home html page
        """
        context = super().get_context_data(**kwargs)
        name = self.request.user.first_name
        user_id = self.request.user.id
        context['name'] = name
        context['user_id'] = user_id
        return context


from rest_framework.exceptions import APIException


class GetFavouriteImages(APIView):
    """
              return requested user favourite images
              else show an error message
       """

    def get(self, request, *args, **kwargs):
        """
            Get the user_id from param and will give corresponding user's favourite images
            else exception if any error

            method type : get
            Param : user_id
            Return : [favourite_images]
            Rtype : Response
        """
        try:
            user_id = request.query_params.get("user_id")
            user = User.objects.get(id=user_id)
            favourite_images = list(
                user.favourite_set.all().order_by("-genDate").values_list("image_url", flat=True))
            return Response({"favourite_images": favourite_images}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"User": "No user available"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # return APIException(e)


class LocationList(APIView):
    """
           Return Location list present in database with given term

    """

    def get(self, request, *args, **kwargs):
        """
               Get the term from param and will give Location list matches to the term
               else exception if any error

                method type : get
                Param : term
                Return : [location name]
                Rtype : Response
        """
        try:
            search_term = request.query_params.get("term")
            location_names = list(Location.objects.filter(name__contains=search_term).values_list("name", flat=True))
            return Response(location_names, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GeoLocationFromLatLong(APIView):
    """
           Return location name by longitude and latitude and if location present in db then return that location name
           else insert in db ,if any error happen in this process will give Exception

    """

    def get(self, request, *args, **kwargs):
        """
               Return location name by longitude and latitude and if location present in db then return that location name
               or insert in db else return error if any

                method type : get
                Param : latitude, longitude
                Return : location_name
                Rtype : json response

        """
        try:
            latitude = request.query_params.get("latitude")
            longitude = request.query_params.get("longitude")

            geo_location_service = GeoLocation()
            location_name = geo_location_service.get_geo_location(latitude, longitude)

            searched_item = list(Location.objects.filter(name=location_name).values_list("name", flat=True))
            if not searched_item:
                Location.objects.create(name=location_name, genDate=timezone.now())
            return Response({"location_name": location_name}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LikeUnlike(APIView):
    """
           Return response status for like and unlike
           if image url is present in db for request user then it will delete
           else insert that url for requested user

    """

    def post(self, request, *args, **kwargs):
        """
              Return response status for like and unlike
              if image url is present in db for request user then it will delete
              else insert that url for requested user

               method type : post
               Param : image_url,user_id
               Return : status
               Rtype : Response

        """
        try:
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
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetLocationByParamAndInsert(APIView):
    """
           Return searched input list  if input is present in db
           otherwise it will insert that input in db and return that input
    """

    def get(self, request, *args, **kwargs):
        """
               Return searched input list  if input is present in db
               otherwise it will insert that input in db and return that input
               else error if any

                method type : get
                Param : term
                Return : images, page, total_pages, favourite_images
        """
        try:
            search_term = request.query_params.get("term")
            searched_items = list(Location.objects.filter(name__contains=search_term).values_list("name", flat=True))
            if searched_items:
                return Response(searched_items, status=status.HTTP_200_OK)
            else:
                Location.objects.create(name=search_term, genDate=timezone.now())
                searched_items.append(search_term)
                return Response(searched_items, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchImages(APIView):
    """
           Return search Images by location name with page ,if page number given
           otherwise page number 1

    """

    def post(self, request, *args, **kwargs):
        """
             Return search Images by location name with page ,if page number given
             otherwise page number 1

              method type : get
              Param : location_name, page_number
              Return : images, page, total_pages, favourite_images
              Rtype : json response

          """
        try:
            user_id = request.data["user_id"]
            if request.data['location_name'] == "":
                location_name = None
            else:
                location_name = request.data['location_name']
            page_number = request.data['page_number']
            flickr_service = FlickrData()
            image_data, page, total_pages = flickr_service.search_image_data(page_number, location_name)
            user = User.objects.get(id=user_id)
            favourite_images = list(
                user.favourite_set.all().order_by("-genDate").values_list("image_url", flat=True))
            for image in image_data:
                if image[0] in favourite_images:
                    image.append(True)
                else:
                    image.append(False)
            return Response(
                {"imageData": image_data, "page": page, "total_pages": total_pages}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"User": "No user Available"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
