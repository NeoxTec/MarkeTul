from django.shortcuts import render,redirect
from django.db.models import Q
from admin_dash.models import Producto, Tienda, Administrador
from django.contrib.auth.models import User
from vendedor.models import Vendedor,SolicitudesVendedor,Catalogo
from django.core.files.storage import FileSystemStorage

idAdmin = 0
idUser = 0
idTienda = 0
# Create your views here.
""" Dashboard Administrador """

def admin_dash(request):
    userid = request.user.id
    global idUser
    idUser = userid
    id_usuario = User.objects.get(id=userid)
    print(str(userid))
    conteo = Administrador.objects.filter(idUser_id=userid).count()
    conteo2 = Vendedor.objects.filter(idUser_id=userid).count()
    if (conteo!=1 and id_usuario.is_staff):
        nadmin = Administrador(nombreAdmin=id_usuario.first_name,idUser_id=userid,correoAdmin=id_usuario.email)
        nadmin.save()
        ida = Administrador.objects.get(idUser_id=userid)
    elif (conteo2!=1 and not id_usuario.is_staff):
        vendedor = Vendedor(nombreVend=id_usuario.first_name,idUser_id=userid,correo=id_usuario.email)
        vendedor.save()
        ida = Vendedor.objects.get(idUser_id=userid)
    else:
        if (id_usuario.is_staff):
            ida= Administrador.objects.get(idUser_id=userid)#llama a admin1
        elif(not id_usuario.is_staff):
            ida = Vendedor.objects.get(idUser_id=userid)
            ida.id = ida.idVend
        global idAdmin #toma variable global para cambiarla
        idAdmin = int(ida.id) #cambia el valor de la variable global para consultas posteriores
        #print(str(idAdmin)) #comprueba cambio
    print("ID_USER:" + str(idAdmin))
    return render(request, "admin_dash/admin_dash.html",{'ida':ida})

def vendedores(request):
    tienda = Tienda.objects.get(idAdmin_id=idAdmin)
    solicitudes = SolicitudesVendedor.objects.filter(idTi_id=tienda.idTi)
    return render(request, "admin_dash/vendedores.html",{'solicitudes':solicitudes})

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
    idad = idAdmin
    name = request.POST['nombreTi'],
    image = request.FILES['logoTi']
    idTienda = Tienda.objects.last()
    print("Ultima tienda registrada es: " + str(idTienda.idTi + 1))

    #Almacenamiento de imagen
    nati = request.FILES['logoTi'] #toma el documento que se sube
    fs = FileSystemStorage(location='media/tienda') #indica ruta de almacenamiento
    print("nombre: " + nati.name +" peso: " + str(nati.size) ) #verifica datos de archivo
    fs.save(str(nati.name),nati) #almacena el archivo con su nombre original y tipo de archivo

    Tienda(idAdmin_id=idad, idTi=idTienda.idTi + 1,nombreTi=str(name[0]),logoTi=str(image[0])).save()

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
    image = request.FILES['imagenProd'],
    marca = request.POST['marcaProd'],
    precio = request.POST['precioProd'],
    medidas = request.POST['medidasProd'],
    existencias = request.POST['existenciasProd'],
    existencias = int(str(existencias[0]))

    #Almacenamiento de imagen
    nami = request.FILES['imagenProd'] #toma el documento que se sube
    fs = FileSystemStorage(location='media/productos') #indica ruta de almacenamiento
    print("nombre: " + nami.name +" peso: " + str(nami.size) ) #verifica datos de archivo
    fs.save(str(nami.name),nami) #almacena el archivo con su nombre original y tipo de archivo

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
    print("ID_USER:" + str(idAdmin))
    tienda = Tienda.objects.get(idAdmin_id=idAdmin)
    solicitudes = SolicitudesVendedor.objects.filter(idTi_id=tienda.idTi)
    return render(request, "admin_dash/admin_solicitudes_vendedor.html",{'solicitudes':solicitudes})

def admin_detalle_solicitud(request,idSolVen):
    solicitud = SolicitudesVendedor.objects.get(idSolVen=idSolVen)
    return render(request, "admin_dash/admin_detalle_solicitud.html",{'solicitud':solicitud})

def cambiar_status_solicitud(request,idSolVen):
    cambio = 1
    sol = SolicitudesVendedor.objects.filter(idSolVen=idSolVen).update(status=cambio)
    tienda = Tienda.objects.get(idAdmin_id=idAdmin)

    solicitud = SolicitudesVendedor.objects.get(idSolVen=idSolVen)
    categoria = "Computo",
    status_nuevo = 1
    idVendedor = int(str(solicitud.idVen_id))
    idTienda = tienda.idTi

    catalogo = Catalogo(categoria=categoria,status=status_nuevo,idVen_id=idVendedor,idTien_id=idTienda).save()

    solicitudes = SolicitudesVendedor.objects.filter(idTi_id=tienda.idTi)

    return render(request, "admin_dash/admin_solicitudes_vendedor.html",{'solicitudes':solicitudes})


def admin_rechazo_solicitud(request):
    return render(request, "admin_dash/admin_rechazo_solicitud.html")

def config_admin(request):
    #print ("id del admin es: " +  str(idAdmin))
    datos_admin = Administrador.objects.get(idUser_id=idAdmin)
    return render(request, "admin_dash/config_admin.html",{'datos':datos_admin})

def update_config(request):
    nombre = request.POST['nombreAdmin'],
    direccion = request.POST['direccionAdmin'],
    telefono = request.POST['telefonoAdmin'],
    correo = request.POST['correoAdmin']
    telefono = int(str(telefono[0]))
    # Objeto del modelo
    config = Administrador.objects.filter(idUser_id = idAdmin).update(nombreAdmin=str(nombre[0]),direccionAdmin=str(direccion[0]),
                                          telefonoAdmin=telefono,correoAdmin=str(correo))
    datos_admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/config_admin.html",{'datos':datos_admin})
