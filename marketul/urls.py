"""marketul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views as web_views
urlpatterns = [
    path('',web_views.home, name="home"),
    path('admin/', admin.site.urls),
    path('acceso/',web_views.acceso, name="acceso"),
    path('perfil_admin/',web_views.perfil_admin, name="perfil_admin"),
    path('perfil_vendedor/',web_views.perfil_vendedor, name="perfil_vendedor"),
    path('perfil_admin/',web_views.perfil_consumidor, name="perfil_consumidor"),
    path('admin_dash/',web_views.admin_dash, name="admin_dash"),
    path('vendedor_dash/',web_views.vendedor_dash, name="vendedor_dash"),
    path('tiendas/',web_views.tiendas, name="tiendas"),
    path('vendedores/',web_views.vendedores, name="vendedores"),
]
