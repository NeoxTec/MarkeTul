from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

""" Dashboard Vendedor"""

class VendorHomeView(TemplateView):
    template_name = "vendedor/vendedor_dash.html"

def tiendas(request):
    return render(request, "vendedor/tiendas.html")

def catalogos_vendedor(request):
    return render(request, "vendedor/catalogos_vendedor.html")

def editar_catalogo(request):
    return render(request, "vendedor/editar_catalogo.html")

def catalogo_tienda(request):
    return render(request, "vendedor/catalogo_tienda.html")

def vendedor_nueva_solicitud(request):
    return render(request, "vendedor/vendedor_nueva_solicitud.html") 

def vendedor_solicitudes(request):
    return render(request, "vendedor/vendedor_solicitudes.html") 

def vendedor_ventas(request):
    return render(request, "vendedor/vendedor_ventas.html") 

def config_vendedor(request):
    return render(request, "vendedor/config_vendedor.html") 
