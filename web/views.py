from django.shortcuts import render, HttpResponse

# Create your views here.

"""Página de Inicio"""
def home(request):
    return render(request, "sitio_web/home.html")

def acceso(request):
    return render(request, "sitio_web/acceso.html")

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

def admin_solicitud_rechazo(request):
    return render(request, "sitio_web/admin_solicitud_rechazo.html") 

def config_admin(request):
    return render(request, "sitio_web/config_admin.html") 

""" Dashboard Vendedor"""

def vendedor_dash(request):
    return render(request, "sitio_web/vendedor_dash.html")

def tiendas(request):
    return render(request, "sitio_web/tiendas.html")

def vendedor_nueva_solicitud(request):
    return render(request, "sitio_web/vendedor_nueva_solicitud.html") 

def vendedor_solicitudes(request):
    return render(request, "sitio_web/vendedor_solicitudes.html") 

