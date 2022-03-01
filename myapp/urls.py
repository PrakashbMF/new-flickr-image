from django.urls import path

from myapp.views import InsertLocation, LikeUnlike, SearchImages, GeoLocationFromLatLong, \
    CreateUser, Signup, Signin, Home, FavouriteImage, GetLocationByParamAndInsert, SignOut

urlpatterns = [
    path('signup/', Signup.as_view(), name="signup"),
    path('create-user/', CreateUser.as_view(), name="create-user"),
    path('signin/', Signin.as_view(), name="signin"),
    path('home/', Home.as_view(), name="home"),
    path('location-list-insert/', GetLocationByParamAndInsert.as_view(), name='location-list-insert'),
    path('insert-location/', InsertLocation.as_view(), name="insert-location"),
    path('like-unlike/', LikeUnlike.as_view(), name='like-unlike'),
    path('search-images/', SearchImages.as_view(), name="search-images"),
    path('geolocation/', GeoLocationFromLatLong.as_view(), name='geolocation'),
    path('favourite-image/', FavouriteImage.as_view(), name='favourite-image'),
    path('signout/', SignOut.as_view(), name="signout"),

]
