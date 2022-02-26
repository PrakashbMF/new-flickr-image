from django.urls import path

from myapp import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('create-user/', views.create_user, name="create-user"),
    path('signin/', views.signin, name="signin"),
    path('log-in/', views.log_in, name="log-in"),
    path('home/', views.home, name="home"),
    path('log-out/', views.log_out, name="log-out"),

]
