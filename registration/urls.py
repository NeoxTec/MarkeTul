from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.registro, name="signup"),
    path('login/',views.login,name="login")
]