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
    path('categorias/',web_views.categorias, name="categorias"),
    path('compras/',web_views.compras, name="compras"),
    path('carrito_compras/',web_views.carrito_compras, name="carrito_compras"),
    path('detalle_producto/',web_views.detalle_producto, name="detalleproducto"),
    path('configuracion_cuenta/',web_views.configuracion_cuenta, name="configuracion_cuenta"),
    path('categoria_computo/',web_views.categoria_computo, name="categoria_computo"),
    path('direccion_envio/',web_views.direccion_envio, name="direccion_envio"),
    path('forma_pago/',web_views.forma_pago, name="forma_pago"),
    path('proceso_pago/',web_views.proceso_pago, name="proceso_pago"),
    path('admin/', admin.site.urls),
    path('acceso/',web_views.acceso, name="acceso"),
    path('perfil_admin/',web_views.perfil_admin, name="perfil_admin"),
    path('perfil_vendedor/',web_views.perfil_vendedor, name="perfil_vendedor"),
    path('perfil_admin',web_views.perfil_consumidor, name="perfil_consumidor"),
    path('pago_error/',web_views.pago_error, name="pago_erro"),
    path('pago_exitoso/',web_views.pago_exitoso, name="pago_exitoso"),
    path('catalogos/',web_views.catalogos, name="catalogos"),
    path('perfil_admin/',web_views.perfil_consumidor, name="perfil_consumidor"),
    path('vendedor_dash/',web_views.vendedor_dash, name="vendedor_dash"),
    path('tiendas/',web_views.tiendas, name="tiendas"),
    path('vendedor_nueva_solicitud/',web_views.vendedor_nueva_solicitud, name="vendedor_nueva_solicitud"),
    path('vendedor_solicitudes/',web_views.vendedor_solicitudes, name="vendedor_solicitudes"),
    path('catalogos_vendedor/',web_views.catalogos_vendedor, name="catalogos_vendedor"),
    path('editar_catalogo/',web_views.editar_catalogo, name="editar_catalogo"),
    path('catalogo_tienda/',web_views.catalogo_tienda, name="catalogo_tienda"),
    path('vendedor_ventas/',web_views.vendedor_ventas, name="vendedor_ventas"),
    path('config_vendedor/',web_views.config_vendedor, name="config_vendedor"),
    

]
