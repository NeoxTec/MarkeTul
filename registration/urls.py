from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.registerPage, name="signup"),
    path('login/',views.loginPage,name="login")
]