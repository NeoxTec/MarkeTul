from django.urls import path
from . import views as admin_views

urlpatterns = [
    # Paths de admin
    path('admin_dash/',admin_views.admin_dash, name="admin_dash"),
    path('admin_solicitudes_vendedor/',admin_views.admin_solicitudes_vendedor, name="admin_solicitudes_vendedor"),
    path('admin_detalle_solicitud/', admin_views.admin_detalle_solicitud, name="admin_detalle_solicitud"),
    path('admin_rechazo_solicitud/',admin_views.admin_rechazo_solicitud, name="admin_rechazo_solicitud"),
    path('admin_tiendas/', admin_views.admin_tiendas, name="admin_tiendas"),
    path('admin_nueva_tienda/', admin_views.admin_nueva_tienda, name="admin_nueva_tienda"),
    path('admin_detalle_tienda/', admin_views.admin_detalle_tienda, name="admin_detalle_tienda"),
    path('admin_productos/',admin_views.admin_productos, name="admin_productos"),
    path('tienda_productos/<id>', admin_views.admin_productos_tienda, name="admin_productos_tienda"),
    path('admin_nuevo_producto/',admin_views.admin_nuevo_producto, name="admin_nuevo_producto"),
    path('nuevos_registro/', admin_views.nuevo_registro, name="nuevo_registro"),#post de agregar producto
    path('actualizacion_producto/', admin_views.actualizacion_producto, name="actualizacion_producto"),  # post de update product
    path('producto_eliminado/',admin_views.producto_eliminado, name="producto_eliminado"),
    path('admin_detalle_producto/<id>',admin_views.admin_detalle_producto, name="admin_detalle_producto"),
    path('config_admin/', admin_views.config_admin, name="config_admin"),
    path('vendedores/',admin_views.vendedores, name="vendedores"),
    path('nueva_tienda/',admin_views.admin_tiendas, name='nueva_tienda'),
]