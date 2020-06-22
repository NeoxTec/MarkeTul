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
    path('admin/', admin.site.urls),
    path('',web_views.home, name="home"),
    path('categorias/',web_views.categorias, name="categorias"),
    path('compras/',web_views.compras, name="compras"),
    path('carrito_compras/',web_views.carrito_compras, name="carrito_compras"),
    path('detalle_producto/',web_views.detalle_producto, name="detalleproducto"),
    path('configuracion_cuenta/',web_views.configuracion_cuenta, name="configuracion_cuenta"),
    path('categoria_computo/',web_views.categoria_computo, name="categoria_computo"),
    path('direccion_envio/',web_views.direccion_envio, name="direccion_envio"),
    path('forma_pago/',web_views.forma_pago, name="forma_pago"),
    path('proceso_pago/',web_views.proceso_pago, name="proceso_pago"),
    
    
]
