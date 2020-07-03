from django.urls import path
from . import views as web_views

urlpatterns = [
    # Paths de web_inicio
    path('',web_views.home, name="home"),
    #path('acceso/',web_views.acceso, name="acceso"),
    path('perfil_admin/',web_views.perfil_admin, name="perfil_admin"),
    path('perfil_vendedor/',web_views.perfil_vendedor, name="perfil_vendedor"),
    path('perfil_consumidor/',web_views.perfil_consumidor, name="perfil_consumidor"),
]