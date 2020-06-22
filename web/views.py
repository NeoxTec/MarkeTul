from django.shortcuts import render, HttpResponse

# Create your views here.

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