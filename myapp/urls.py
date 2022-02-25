from django.urls import path

from myapp import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
]
