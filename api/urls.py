from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('ventas-list/', views.ventasList, name="ventas-list"),
    path('config-admin/', views.config_admin, name="config-admin"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('vendedor-config/', views.vendedor_config, name="vendedor-config"),
    path('consumidor-config/', views.consumidor_config, name="consumidor-config"),
]
