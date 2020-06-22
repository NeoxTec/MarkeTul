from django.shortcuts import render, HttpResponse

# Create your views here.

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

def admin_dash(request):
    return render(request, "sitio_web/admin_dash.html")