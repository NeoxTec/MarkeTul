from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from admin_dash.models import Producto,Tienda,Administrador
from vendedor.models import Vendedor,SolicitudesVendedor

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

def vendedor_nueva_solicitud(request, idTi):
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    datos_vendedor = Vendedor.objects.get(idUser_id=userid)
    tienda = Tienda.objects.get(idTi=idTi)
    return render(request, "vendedor/vendedor_nueva_solicitud.html",{'datos':datos_vendedor,'tienda':tienda}) 

def vendedor_solicitudes(request):
    return render(request, "vendedor/vendedor_solicitudes.html") 

def vendedor_ventas(request):
    return render(request, "vendedor/vendedor_ventas.html") 

def config_vendedor(request):
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    datos_vendedor = Vendedor.objects.get(idUser_id=userid)
    return render(request, "vendedor/config_vendedor.html", {'datos':datos_vendedor}) 

def guardar_config(request):
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    nombre = request.POST['nombreVend'],
    telefono = request.POST['telefono'],
    correo = request.POST['correo']
    telefono = int(str(telefono[0]))
    configuracion = Vendedor.objects.filter(idUser_id = userid).update(nombreVend=str(nombre[0]), telefono=telefono, correo=str(correo))

    datos_vendedor = Vendedor.objects.get(idUser_id=userid)
    return render(request, "vendedor/config_vendedor.html", {'datos':datos_vendedor}) 

def enviar_solicitud(request,idTi):
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    vendedor = Vendedor.objects.get(idUser_id=userid)
    tienda = Tienda.objects.get(idTi=idTi)
    nombre = request.POST['nombreV'],
    direccion = request.POST['direccionV'],
    correo = request.POST['correoV'],
    edad = request.POST['edadVend'],
    edad = int(str(edad[0]))
    genero = request.POST['genero'],
    motivo = request.POST['motivos'],

    sol = SolicitudesVendedor(nombreV=str(nombre[0]), direccionV=str(direccion), correoV = str(correo),
                edadVen=edad, genero=str(genero[0]), motivos=str(motivo), idTi_id=tienda.idTi, idVen_id=vendedor.idVend).save()

    return render(request, "vendedor/vendedor_solicitudes.html")

