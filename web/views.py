from django.shortcuts import render, HttpResponse

# Create your views here.

"""Página de Inicio"""
def home(request):
    return render(request, "sitio_web/home.html")
def categorias(request):
    return render(request, "sitio_web/categorias.html")
def compras(request):
    return render(request, "sitio_web/compras.html")
def carrito_compras(request):
    return render(request, "sitio_web/carrito_compras.html")
def detalle_producto(request):
    return render(request, "sitio_web/detalle_producto.html")
def configuracion_cuenta(request):
    return render(request, "sitio_web/configuracion_cuenta.html")
def categoria_computo(request):
    return render(request, "sitio_web/categoria_computo.html")
def direccion_envio(request):
    return render(request, "sitio_web/direccion_envio.html")
def forma_pago(request):
    return render(request, "sitio_web/forma_pago.html")
def proceso_pago(request):
    return render(request, "sitio_web/proceso_pago.html")
def pago_error(request):
    return render(request, "sitio_web/pago_error.html")
def pago_exitoso(request):
    return render(request, "sitio_web/pago_exitoso.html")
def acceso(request):
    return render(request, "sitio_web/acceso.html")
def catalogos(request):
    return render(request, "sitio_web/catalogos.html")
def perfil_admin(request):
    return render(request, "sitio_web/perfil_admin.html")

def perfil_vendedor(request):
    return render(request, "sitio_web/perfil_vendedor.html")

def perfil_consumidor(request):
    return render(request, "sitio_web/perfil_consumidor.html")

""" Dashboard Administrador """

def admin_dash(request):
    return render(request, "sitio_web/admin_dash.html")

def vendedores(request):
    return render(request, "sitio_web/vendedores.html")

def admin_productos(request):
    return render(request, "sitio_web/admin_productos.html") 

def admin_detalle_producto(request):
    return render(request, "sitio_web/admin_detalle_producto.html")

def admin_nuevo_producto(request):
    return render(request, "sitio_web/admin_nuevo_producto.html") 

def admin_solicitudes_vendedor(request):
    return render(request, "sitio_web/admin_solicitudes_vendedor.html") 

def admin_detalle_solicitud(request):
    return render(request, "sitio_web/admin_detalle_solicitud.html") 

def admin_rechazo_solicitud(request):
    return render(request, "sitio_web/admin_rechazo_solicitud.html") 

def config_admin(request):
    return render(request, "sitio_web/config_admin.html") 

""" Dashboard Vendedor"""

def vendedor_dash(request):
    return render(request, "sitio_web/vendedor_dash.html")

def tiendas(request):
    return render(request, "sitio_web/tiendas.html")

def catalogos_vendedor(request):
    return render(request, "sitio_web/catalogos_vendedor.html")

def editar_catalogo(request):
    return render(request, "sitio_web/editar_catalogo.html")

def catalogo_tienda(request):
    return render(request, "sitio_web/catalogo_tienda.html")

def vendedor_nueva_solicitud(request):
    return render(request, "sitio_web/vendedor_nueva_solicitud.html") 

def vendedor_solicitudes(request):
    return render(request, "sitio_web/vendedor_solicitudes.html") 

def vendedor_vendas(request):
    return render(request, "sitio_web/vendedor_vendas.html") 

def config_vendedor(request):
    return render(request, "sitio_web/config_vendedor.html") 

