from django.views.generic.base import TemplateView
from django.shortcuts import render
from admin_dash.models import Producto
from admin_dash.models import Tienda
from admin_dash.models import Administrador

# Create your views here.

""" Dashboard Vendedor"""

class VendorHomeView(TemplateView):
    template_name = "vendedor/vendedor_dash.html"

def tiendas(request):
    listaT = Tienda.objects.all()
    context = {'tiendas': listaT}
    return render(request, "vendedor/tiendas.html", context)

def catalogos_vendedor(request):
    listaT = Tienda.objects.all()
    context = {'tiendas': listaT}
    print (listaT)
    return render(request, "vendedor/catalogos_vendedor.html", context)

def editar_catalogo(request):
    return render(request, "vendedor/editar_catalogo.html")

def editar_catalogo_2(request):
    return render(request, "vendedor/editar_catalogo_2.html")

def editar_catalogo_3(request):
    return render(request, "vendedor/editar_catalogo_3.html")

def catalogo_tienda(request):
    listaP = Producto.objects.all()
    context = {'productos': listaP}
    return render(request, "vendedor/catalogo_tienda.html",context)

def vendedor_nueva_solicitud(request):
    return render(request, "vendedor/vendedor_nueva_solicitud.html") 

def vendedor_solicitudes(request):
    return render(request, "vendedor/vendedor_solicitudes.html") 

def vendedor_ventas(request):
    return render(request, "vendedor/vendedor_ventas.html") 

def config_vendedor(request):
    return render(request, "vendedor/config_vendedor.html") 

def config_vendedor_r(request):
    return render(request, "vendedor/config_vendedor_r.html") 
