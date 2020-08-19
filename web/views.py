from django.shortcuts import render, HttpResponse
from admin_dash.models import Tienda

# Create your views here.

"""Página de Inicio"""
def home(request):
    listaT = Tienda.objects.all()
    context = {'tiendas': listaT}
    for tienda in listaT:
        print("URL:"+str(tienda.logoTi))
    return render(request, "sitio_web/home.html",context)

def acceso(request):
    return render(request, "sitio_web/acceso.html")

def perfil_admin(request):
    return render(request, "sitio_web/perfil_admin.html")

def perfil_vendedor(request):
    return render(request, "sitio_web/perfil_vendedor.html")

def perfil_consumidor(request):
    return render(request, "sitio_web/perfil_consumidor.html")

