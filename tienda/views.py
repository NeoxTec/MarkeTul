from django.shortcuts import render

# Create your views here.

"""Tienda"""

def categorias(request):
    return render(request, "tienda/categorias.html")

def compras(request):
    return render(request, "tienda/compras.html")

def carrito_compras(request):
    return render(request, "tienda/carrito_compras.html")

def detalle_producto(request):
    return render(request, "tienda/detalle_producto.html")

def configuracion_cuenta(request):
    return render(request, "tienda/configuracion_cuenta.html")

def categoria_computo(request):
    return render(request, "tienda/categoria_computo.html")

def direccion_envio(request):
    return render(request, "tienda/direccion_envio.html")

def forma_pago(request):
    return render(request, "tienda/forma_pago.html")

def proceso_pago(request):
    return render(request, "tienda/proceso_pago.html")

def pago_error(request):
    return render(request, "tienda/pago_error.html")

def pago_exitoso(request):
    return render(request, "tienda/pago_exitoso.html")

def catalogos(request):
    return render(request, "tienda/catalogos.html")

