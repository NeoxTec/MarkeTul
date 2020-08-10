from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from admin_dash.models import Producto,Tienda,Administrador
from vendedor.models import Vendedor,SolicitudesVendedor,Catalogo, CatalogoProducto
from registration.models import Usuario_Tipo

from django.contrib import messages

from registration.views import login,loginPage

from django.contrib.auth.decorators import login_required

# Create your views here.


""" Dashboard Vendedor"""

class VendorHomeView(TemplateView):
    template_name = "vendedor/vendedor_dash.html"

@login_required(login_url='login')
def tiendas(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    listaT = Tienda.objects.all()
    context = {'tiendas': listaT,'tipo':tipo}
    return render(request, "vendedor/tiendas.html", context)

@login_required(login_url='login')
def catalogos_vendedor(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    vendedor = Vendedor.objects.get(idUser_id=userid)
    listaC = Catalogo.objects.filter(idVen_id=vendedor.idVend)
    context = {'catalogos': listaC,'tipo':tipo} # Corregir
    return render(request, "vendedor/catalogos_vendedor.html", context)

@login_required(login_url='login')
def editar_catalogo(request,idCatal):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
    catalogo = Catalogo.objects.get(idCatal=idCatal)
    return render(request, "vendedor/editar_catalogo.html",{'productos':productos,'catalogo':catalogo,'tipo':tipo})

@login_required(login_url='login')
def catalogo_tienda_sn(request,idTi):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    listaP = Producto.objects.filter(idTi_id=idTi)
    context = {'productos': listaP,'tipo':tipo}
    return render(request, "vendedor/catalogo_tienda_sn.html",context)

def editar_catalogo_2(request):
    return render(request, "vendedor/editar_catalogo_2.html")

def editar_catalogo_3(request):
    return render(request, "vendedor/editar_catalogo_3.html")

@login_required(login_url='login')
def catalogo_tienda(request,idTi,idCatal):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    listaP = Producto.objects.filter(idTi_id=idTi)
    context = {'productos': listaP,'idCatal':idCatal,'tipo':tipo}
    idCatal = idCatal
    for producto in listaP:
        print(producto.imagenProd)
    return render(request, "vendedor/catalogo_tienda.html",context)

@login_required(login_url='login')
def añadir_producto_catalogo(request,idProd,idCatal):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    catalogo_producto = CatalogoProducto(idCatalogo_id=idCatal,idProducto_id=idProd).save()
    listaC = Catalogo.objects.all()
    context = {'catalogos': listaC,'tipo':tipo}
    return render(request, "vendedor/catalogos_vendedor.html", context)

@login_required(login_url='login')
def vendedor_nueva_solicitud(request, idTi):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    datos_vendedor = Vendedor.objects.get(idUser_id=userid)
    tienda = Tienda.objects.get(idTi=idTi)
    return render(request, "vendedor/vendedor_nueva_solicitud.html",{'datos':datos_vendedor,'tienda':tienda,'tipo':tipo}) 

@login_required(login_url='login')
def vendedor_solicitudes(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    vendedor = Vendedor.objects.get(idUser_id=userid)
    solicitudes = SolicitudesVendedor.objects.filter(idVen_id=vendedor.idVend).values('idTi_id','status','idTi_id__nombreTi','idSolVen')
    return render(request, "vendedor/vendedor_solicitudes.html",{'solicitudes':solicitudes,'tipo':tipo}) 

@login_required(login_url='login')
def vendedor_ventas(request):
    return render(request, "vendedor/vendedor_ventas.html") 

@login_required(login_url='login')
def config_vendedor(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)
    datos_vendedor = Vendedor.objects.get(idUser_id=userid)
    return render(request, "vendedor/config_vendedor.html", {'datos':datos_vendedor,'tipo':tipo}) 

@login_required(login_url='login')
def guardar_config(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    usuario = User.objects.get(id=userid)
    nombre = request.POST['nombreVend'],
    telefono = request.POST['telefono'],
    correo = request.POST['correo']
    telefono = int(str(telefono[0]))
    nc = request.POST['nc']
    cc = request.POST['cc']
    configuracion = Vendedor.objects.filter(idUser_id = userid).update(nombreVend=str(nombre[0]), telefono=telefono, correo=str(correo))

    if nc and nc == cc:
        usuario.set_password(nc)
        usuario.save()
        messages.info(request,"Contraseña cambiada correctamente")
    elif nc and nc != cc:
        messages.info(request,"Contraseñas no coinciden")

    datos_vendedor = Vendedor.objects.get(idUser_id=userid)
    return render(request, "vendedor/config_vendedor.html", {'datos':datos_vendedor,'tipo':tipo}) 

@login_required(login_url='login')
def enviar_solicitud(request,idTi):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
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

    sol = SolicitudesVendedor(nombreV=str(nombre[0]), direccionV=direccion, correoV = correo,
                edadVen=edad, genero=str(genero[0]), motivos=str(motivo), idTi_id=tienda.idTi, idVen_id=vendedor.idVend, noadmin= tienda.idAdmin_id).save()

    return render(request, "vendedor/vendedor_solicitudes.html")

