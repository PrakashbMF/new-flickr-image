from django.urls import path

from myapp import views
from myapp.views import InsertLocation, LocationList, LikeUnlike, SearchImages, GeoLocationFromLatLong, \
    CreateUser, Signup, Signin, Home, FavouriteImage, GetLocationByParamAndInsert, SignOut

urlpatterns = [
    path('signup/', Signup.as_view(), name="signup"),
    # path('welcome/', views.welcome, name="welcome"),
    # path('create-user/', views.create_user, name="create-user"),
    path('create-user/', CreateUser.as_view(), name="create-user"),
    # path('signin/', views.signin, name="signin"),
    path('signin/', Signin.as_view(), name="signin"),
    # path('log-in/', views.log_in, name="log-in"),
    # path('home/', views.home, name="home"),
    path('home/', Home.as_view(), name="home"),
    # path('location-list/', LocationList.as_view(), name='location-list'),
    # path('location-list/<str:name>/', LocationList.as_view(), name='location-list'),
    # path('location-list-insert/<str:name>/', GetLocationByParamAndInsert.as_view(), name='location-list-insert'),
    path('location-list-insert/', GetLocationByParamAndInsert.as_view(), name='location-list-insert'),

    path('insert-location/', InsertLocation.as_view(), name="insert-location"),

    path('like-unlike/', LikeUnlike.as_view(), name='like-unlike'),
    # path('like-unlike/<str:image_url>/', LikeUnlike.as_view(), name='like-unlike'),
    # path('favourite-image/<int:user_id>', FavouriteImages.as_view(), name='favourite-image'),
    path('search-images/', SearchImages.as_view(), name="search-images"),
    path('geolocation/', GeoLocationFromLatLong.as_view(), name='geolocation'),
    path('favourite-image/', FavouriteImage.as_view(), name='favourite-image'),

    # path('signout/', views.signout, name="signout"),
    path('signout/', SignOut.as_view(), name="signout"),

]
