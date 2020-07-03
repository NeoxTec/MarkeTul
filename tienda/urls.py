from django.urls import path
from . import views as tienda_views

urlpatterns = [
    # Paths de Tienda
    path('categorias/',tienda_views.categorias, name="categorias"),
    path('compras/',tienda_views.compras, name="compras"),
    path('carrito_compras/',tienda_views.carrito_compras, name="carrito_compras"),
    path('detalle_producto/',tienda_views.detalle_producto, name="detalleproducto"),
    path('configuracion_cuenta/',tienda_views.configuracion_cuenta, name="configuracion_cuenta"),
    path('categoria_computo/',tienda_views.categoria_computo, name="categoria_computo"),
    path('direccion_envio/',tienda_views.direccion_envio, name="direccion_envio"),
    path('forma_pago/',tienda_views.forma_pago, name="forma_pago"),
    path('proceso_pago/',tienda_views.proceso_pago, name="proceso_pago"),
    path('pago_error/',tienda_views.pago_error, name="pago_erro"),
    path('pago_exitoso/',tienda_views.pago_exitoso, name="pago_exitoso"),
    path('catalogos/',tienda_views.catalogos, name="catalogos"),
    path('carrito_compras2/',tienda_views.carrito_compras2, name="carrito_compras2"),
    
    

]