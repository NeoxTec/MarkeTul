from django.shortcuts import render

# Create your views here.

"""Tienda"""

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

def catalogos(request):
    return render(request, "sitio_web/catalogos.html")