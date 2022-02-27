from django.urls import path

from myapp import views
from myapp.views import InsertLocation, LocationList, LikeUnlike, FavouriteImages, SearchImages, GeoLocationFromLatLong

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('welcome/', views.welcome, name="welcome"),
    path('create-user/', views.create_user, name="create-user"),
    path('signin/', views.signin, name="signin"),
    # path('log-in/', views.log_in, name="log-in"),
    path('home/', views.home, name="home"),
    path('location-list/<str:name>/', LocationList.as_view(), name='location-list'),

    path('insert-location/', InsertLocation.as_view(), name="insert-location"),

    path('like-unlike/', LikeUnlike.as_view(), name='like-unlike'),
    # path('like-unlike/<str:image_url>/', LikeUnlike.as_view(), name='like-unlike'),
    path('favourite-image/<int:user_id>', FavouriteImages.as_view(), name='favourite-image'),
    path('search-images/', SearchImages.as_view(), name="search-images"),
    path('geolocation/', GeoLocationFromLatLong.as_view(), name='geolocation'),

    path('signout/', views.signout, name="signout"),

]
