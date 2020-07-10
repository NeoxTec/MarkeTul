from django.shortcuts import render,redirect
from django.db.models import Q
from admin_dash.models import Producto, Tienda, Administrador
from django.contrib.auth.models import User

idAd = 0
idTienda = 0
# Create your views here.
""" Dashboard Administrador """

def admin_dash(request):
    userid = request.user.id
    id_usuario = User.objects.get(id=userid)#datos usuario
    print(str(id_usuario.id))
    ida= Administrador.objects.get(id=1)#llama a admin1 
    global idAd #toma variable global para cambiarla
    idAd = int(ida.id) #cambia el valor de la variable global para consultas posteriores
    #print(str(idAdmin)) #comprueba cambio
    return render(request, "admin_dash/admin_dash.html",{'ida':ida})

def vendedores(request):
    return render(request, "admin_dash/vendedores.html")

def admin_productos(request):
    listaP = Producto.objects.all()
    print (listaP)
    return render(request, "admin_dash/admin_productos.html", {'productos': listaP})

def admin_productos_tienda(request,id):
    listaP = Producto.objects.filter(Q(idTi_id=id)&Q(estado=1))
    global idTienda
    idTienda = id
    print(idTienda)
    return render(request, "admin_dash/admin_productos.html", {'productos': listaP})

def admin_tiendas(request):
    print(idAdmin)
    listaT = Tienda.objects.filter(idAdmin_id=idAdmin)
    admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/admin_tiendas.html",{'tiendas':listaT,'admin':admin})

def admin_nueva_tienda(request):
    print(idAdmin)
    return render(request, "admin_dash/admin_nueva_tienda.html")

def nueva_tienda(request):
    print("admin es:"+ str(idAdmin))
    image = request.POST['logoTi']
    name = request.POST['nombreTi']
    print("archivo es: "+ str(image[0]) + " y la tienda se llama: "+ str(name[0]))
    nueva = Tienda(nombreTi=str(name[0]),logoTi=str(image[0]),idAdmin_id=idAdmin)
    nueva.save()

    listaT = Tienda.objects.filter(idAdmin_id=idAdmin)
    admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/admin_tiendas.html", {'tiendas': listaT, 'admin': admin})


def admin_detalle_tienda(request):
    return render(request, "admin_dash/admin_detalle_tienda.html")

def admin_detalle_producto(request, id):
    prod = Producto.objects.get(idProd=id)
    return render(request, "admin_dash/admin_detalle_producto.html",{'prod':prod})

def admin_nuevo_producto(request):
    idt = Tienda.objects.get(idTi=idTienda)
    return render(request, "admin_dash/admin_nuevo_producto.html",{'idt':idt}) 

def nuevo_registro(request):
    tienda = request.POST['idTi_id'],
    tienda = int(str(tienda[0]))
    nombre= request.POST['nombreProd'],
    descripcion= request.POST['descripcionProd'],
    cat = request.POST['categoriaProd'],
    image = request.POST['imagenProd'],
    marca = request.POST['marcaProd'],
    precio = request.POST['precioProd'],
    medidas = request.POST['medidasProd'],
    existencias = request.POST['existenciasProd'],
    existencias = int(str(existencias[0]))
    #crea objeto
    prod = Producto(nombreProd= str(nombre[0]), categoriaProd= str(cat[0]), imagenProd=str(image[0]),
                    marcaProd=str(marca[0]), descripcionProd=str(descripcion[0]), precioProd=float(precio[0]), 
                    medidasProd=str(medidas[0]), existenciasProd= existencias, idTi_id=tienda)
    
    #guarda objeto en la bd
    prod.save()
    #redirecciona a la pagina
    listaP = Producto.objects.filter(Q(idTi_id=tienda)&Q(estado=1))
    print(tienda)
    return render(request, "admin_dash/admin_productos.html",{'productos':listaP})

def actualizacion_producto(request):
    id = request.POST['idProd'],
    nombre = request.POST['nombreProd'],
    descripcion = request.POST['descripcionProd'],
    cat = request.POST['categoriaProd'],
    marca = request.POST['marcaProd'],
    precio = request.POST['precioProd'],
    precio = float(str(precio[0])),
    medidas = request.POST['medidasProd'],
    existencias = request.POST['existenciasProd'],
    existencias = int(str(existencias[0]))
    #crea objeto
    Producto.objects.filter( idProd=int(str(id[0])) ).update(nombreProd=str(nombre[0]), categoriaProd=str(cat[0]),
                    marcaProd=str(marca[0]), descripcionProd=str(descripcion[0]), precioProd=precio[0],
                    medidasProd=str(medidas[0]), existenciasProd=existencias)
    #guarda objeto en la bd
    listaP = Producto.objects.filter(Q(idTi_id=idTienda) & Q(estado=1))
    print(idTienda)
    #redirecciona a la pagina
    return render(request, "admin_dash/admin_productos.html",{'productos':listaP})

def producto_eliminado(request):
    idp= request.POST['idProd']
    cambio = 0
    pr = Producto.objects.filter( idProd=idp ).update(estado=cambio)

    listaP = Producto.objects.filter(Q(idTi_id=idTienda) & Q(estado=1))
    print ("dato= "+ str(id))
    return render(request,"admin_dash/admin_productos.html",{'productos':listaP})

def admin_solicitudes_vendedor(request):
    return render(request, "admin_dash/admin_solicitudes_vendedor.html") 

def admin_detalle_solicitud(request):
    return render(request, "admin_dash/admin_detalle_solicitud.html") 

def admin_rechazo_solicitud(request):
    return render(request, "admin_dash/admin_rechazo_solicitud.html") 

def config_admin(request):
    #print ("id del admin es: " +  str(idAdmin))
    datos_admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/config_admin.html",{'datos':datos_admin})