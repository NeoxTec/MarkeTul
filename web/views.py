from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "sitio_web/home.html")
def categorias(request):
    return render(request, "sitio_web/categorias.html")
def compras(request):
    return render(request, "sitio_web/compras.html")