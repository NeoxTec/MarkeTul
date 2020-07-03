from django.urls import path
from . import views as vendedor_views
from .views import VendorHomeView

urlpatterns = [
    # Paths de vendedor
    path('vendedor_dash/',VendorHomeView.as_view(), name="vendedor_dash"),
    path('tiendas/',vendedor_views.tiendas, name="tiendas"),
    path('catalogos_vendedor/',vendedor_views.catalogos_vendedor, name="catalogos_vendedor"),
    path('editar_catalogo/',vendedor_views.editar_catalogo, name="editar_catalogo"),
    path('editar_catalogo_2/',vendedor_views.editar_catalogo_2, name="editar_catalogo_2"),
    path('editar_catalogo_3/',vendedor_views.editar_catalogo_3, name="editar_catalogo_3"),
    path('catalogo_tienda/',vendedor_views.catalogo_tienda, name="catalogo_tienda"),
    path('vendedor_nueva_solicitud/',vendedor_views.vendedor_nueva_solicitud, name="vendedor_nueva_solicitud"),
    path('vendedor_solicitudes/',vendedor_views.vendedor_solicitudes, name="vendedor_solicitudes"),
    path('vendedor_ventas/',vendedor_views.vendedor_ventas, name="vendedor_ventas"),
    path('config_vendedor/',vendedor_views.config_vendedor, name="config_vendedor"),
    path('config_vendedor_r/',vendedor_views.config_vendedor_r, name="config_vendedor_r"),
]