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

