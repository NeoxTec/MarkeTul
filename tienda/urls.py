from django.urls import path
from . import views as tienda_views

urlpatterns = [
    # Paths de Tienda
    path('categorias/',tienda_views.categorias, name="categorias"),
    path('compras/',tienda_views.compras, name="compras"),
    path('carrito_compras/<int:idProd>',tienda_views.carrito_compras, name="carrito_compras"),
    path('añadir_producto_carrito/<int:idProd>/<int:idCatal>',tienda_views.añadir_producto_carrito, name="añadir_producto_carrito"),
    path('carrito/',tienda_views.carrito, name="carrito"),
    path('añadir_producto_carrito/<int:idProd>',tienda_views.añadir_producto_carrito, name="añadir_producto_carrito"),
    path('detalle_producto/',tienda_views.detalle_producto, name="detalleproducto"),
    path('configuracion_cuenta/',tienda_views.configuracion_cuenta, name="configuracion_cuenta"),
    path('guardar_config_con/',tienda_views.guardar_config_con, name="guardar_config_con"),
    path('categoria_computo/',tienda_views.categoria_computo, name="categoria_computo"),
    path('categoria_niño/',tienda_views.categoria_niño, name="categoria_niño"),
    path('categoria_hombre/',tienda_views.categoria_hombre, name="categoria_hombre"),
    path('categoria_mujer/',tienda_views.categoria_mujer, name="categoria_mujer"),
    path('categoria_libros/',tienda_views.categoria_libros, name="categoria_libros"),
    path('categoria_mascotas/',tienda_views.categoria_mascotas, name="categoria_mascotas"),
    path('categoria_muebles/',tienda_views.categoria_muebles, name="categoria_muebles"),
    path('categoria_electrodomesticos/',tienda_views.categoria_electrodomesticos, name="categoria_electrodomesticos"),
    path('catalogos/<int:idCatal>',tienda_views.catalogos, name="catalogos"),
    path('direccion_envio/',tienda_views.direccion_envio, name="direccion_envio"),
    path('guardar_direccion/',tienda_views.guardar_direccion, name="guardar_direccion"),
    path('direccion_envio1/',tienda_views.direccion_envio1, name="direccion_envio1"),
    path('forma_pago/',tienda_views.forma_pago, name="forma_pago"),
    path('post_forma_pago/',tienda_views.post_forma_pago, name="post_forma_pago"),
    path('proceso_pago/',tienda_views.proceso_pago, name="proceso_pago"),
    path('pago_error/',tienda_views.pago_error, name="pago_error"),
    path('pago_exitoso/',tienda_views.pago_exitoso, name="pago_exitoso"),
    
    

]