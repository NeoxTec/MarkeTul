from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('ventas-list/', views.ventasList, name="ventas-list"),
    path('config-admin/', views.config_admin, name="config-admin"),
    path('vendedores/', views.vendedores, name="vendedores-api"),
    path('vendedor-config/', views.vendedor_config, name="vendedor-config"),
    path('consumidor-config/', views.consumidor_config, name="consumidor-config"),
    path('categoria-computo/', views.categoria_computo, name="categoria-computo"),
    path('catalogo-productos/<int:idCatal>/', views.catalogo_productos, name="catalogo-productos"),
    path('carrito/', views.carrito, name="carrito-api"),
    path('carrito-productos/', views.carrito_productos, name="carrito-productos"),
]
