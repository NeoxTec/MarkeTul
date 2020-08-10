from django.urls import path
from . import views as vendedor_views
from .views import VendorHomeView

urlpatterns = [
    # Paths de vendedor
    path('vendedor_dash/',VendorHomeView.as_view(), name="vendedor_dash"),
    path('tiendas/',vendedor_views.tiendas, name="tiendas"),
    path('catalogos_vendedor/',vendedor_views.catalogos_vendedor, name="catalogos_vendedor"),
    path('editar_catalogo/<int:idCatal>',vendedor_views.editar_catalogo, name="editar_catalogo"),
    path('cambio_categoria/',vendedor_views.cambio_categoria, name="cambio_categoria"),
    path('eliminar_producto_catalogo/<int:idProd>/<int:idCatal>',vendedor_views.eliminar_producto_catalogo, name="eliminar_producto_catalogo"),
    path('catalogo_tienda/<int:idTi>/<int:idCatal>',vendedor_views.catalogo_tienda, name="catalogo_tienda"),
    path('catalogo_tienda_sn/<int:idTi>/',vendedor_views.catalogo_tienda_sn, name="catalogo_tienda_sn"),
    path('añadir_producto_catalogo/<int:idProd>/<int:idCatal>',vendedor_views.añadir_producto_catalogo, name="añadir_producto_catalogo"),
    path('vendedor_nueva_solicitud/<int:idTi>',vendedor_views.vendedor_nueva_solicitud, name="vendedor_nueva_solicitud"),
    path('enviar_solicitud/<int:idTi>',vendedor_views.enviar_solicitud, name="enviar_solicitud"),
    path('guardar_config/',vendedor_views.guardar_config, name="guardar_config"),
    path('vendedor_solicitudes/',vendedor_views.vendedor_solicitudes, name="vendedor_solicitudes"),
    path('vendedor_ventas/',vendedor_views.vendedor_ventas, name="vendedor_ventas"),
    path('config_vendedor/',vendedor_views.config_vendedor, name="config_vendedor"),
]