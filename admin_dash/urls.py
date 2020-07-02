from django.urls import path
from . import views as admin_views

urlpatterns = [
    # Paths de admin
    path('admin_dash/',admin_views.admin_dash, name="admin_dash"),
    path('admin_solicitudes_vendedor/',admin_views.admin_solicitudes_vendedor, name="admin_solicitudes_vendedor"),
    path('admin_detalle_solicitud/',admin_views.admin_detalle_solicitud, name="admin_detalle_solicitud"),
    path('admin_rechazo_solicitud/',admin_views.admin_rechazo_solicitud, name="admin_rechazo_solicitud"),
    path('admin_productos/',admin_views.admin_productos, name="admin_productos"),
    path('admin_nuevo_producto/',admin_views.admin_nuevo_producto, name="admin_nuevo_producto"),
    path('admin_detalle_producto/',admin_views.admin_detalle_producto, name="admin_detalle_producto"),
    path('config_admin/',admin_views.config_admin, name="config_admin"),
    path('vendedores/',admin_views.vendedores, name="vendedores"),
]