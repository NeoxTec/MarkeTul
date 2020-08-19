from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('ventas-list/', views.ventasList, name="ventas-list"),
    path('admin_config/', views.config_admin, name="config_admin"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('vendedor_config/', views.vendedor_config, name="vendedor_config"),
    path('consumidor_config/', views.consumidor_config, name="consumidor_config"),
]
