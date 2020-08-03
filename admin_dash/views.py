from django.shortcuts import render,redirect
from django.db.models import Q
from admin_dash.models import Producto, Tienda, Administrador
from django.contrib.auth.models import User
from vendedor.models import Vendedor,SolicitudesVendedor,Catalogo
from django.core.files.storage import FileSystemStorage
from registration.models import Usuario_Tipo
from registration.views import login,loginPage

from django.contrib.auth.decorators import login_required

idAdmin = 0
idUser = 0
idTienda = 0
# Create your views here.
""" Dashboard Administrador """

@login_required(login_url='login')
def admin_dash(request):
    userid = request.user.id
    global idUser
    idUser = userid
    id_usuario = User.objects.get(id=userid)
    print("ID:" + str(userid))
    conteo = Administrador.objects.filter(idUser_id=userid).count()
    conteo2 = Vendedor.objects.filter(idUser_id=userid).count()
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    print("TIPO_USUARIO: " + str(tipo.idTipo_User_id))
    if (conteo!=1 and tipo.idTipo_User_id == 1):
        nadmin = Administrador(nombreAdmin=id_usuario.first_name,idUser_id=userid,correoAdmin=id_usuario.email)
        nadmin.save()
        ida = Administrador.objects.get(idUser_id=userid)
    elif (conteo2!=1 and tipo.idTipo_User_id == 2):
        vendedor = Vendedor(nombreVend=id_usuario.first_name,idUser_id=userid,correo=id_usuario.email)
        vendedor.save()
        ida = Vendedor.objects.get(idUser_id=userid)
    else:
        if (tipo.idTipo_User_id == 1):
            ida= Administrador.objects.get(idUser_id=userid)#llama a admin1
        elif(tipo.idTipo_User_id == 2):
            ida = Vendedor.objects.get(idUser_id=userid)
            ida.id = ida.idVend
        global idAdmin #toma variable global para cambiarla
        idAdmin = int(ida.id) #cambia el valor de la variable global para consultas posteriores
        #print(str(idAdmin)) #comprueba cambio
    print("ID_USER:" + str(idAdmin))
    return render(request, "admin_dash/admin_dash.html",{'ida':ida,'tipo':tipo})

@login_required(login_url='login')
def vendedores(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    tienda = Tienda.objects.get(idAdmin_id=idAdmin)
    solicitudes = SolicitudesVendedor.objects.filter(idTi_id=tienda.idTi)
    return render(request, "admin_dash/vendedores.html",{'solicitudes':solicitudes,'tipo':tipo})

@login_required(login_url='login')
def admin_productos(request):
    listaP = Producto.objects.all()
    print (listaP)
    return render(request, "admin_dash/admin_productos.html", {'productos': listaP})

@login_required(login_url='login')
def admin_productos_tienda(request,id):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    listaP = Producto.objects.filter(Q(idTi_id=id)&Q(estado=1))
    global idTienda
    idTienda = id
    print(idTienda)
    return render(request, "admin_dash/admin_productos.html", {'productos': listaP,'tipo':tipo  })

@login_required(login_url='login')
def admin_tiendas(request):
    print(idAdmin)
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    listaT = Tienda.objects.filter(idAdmin_id=idAdmin)
    admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/admin_tiendas.html",{'tiendas':listaT,'admin':admin,'tipo':tipo})

@login_required(login_url='login')
def admin_nueva_tienda(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
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

    Tienda(idAdmin_id=idad, idTi=idTienda.idTi + 1,nombreTi=str(name[0]),logoTi="tienda/"+ str(nati.name)).save()

    listaT = Tienda.objects.filter(idAdmin_id=idAdmin)
    admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/admin_tiendas.html", {'tiendas': listaT, 'admin': admin,'tipo':tipo})


def admin_detalle_tienda(request):
    return render(request, "admin_dash/admin_detalle_tienda.html")

@login_required(login_url='login')
def admin_detalle_producto(request, id):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    prod = Producto.objects.get(idProd=id)
    return render(request, "admin_dash/admin_detalle_producto.html",{'prod':prod,'tipo':tipo})

@login_required(login_url='login')
def admin_nuevo_producto(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    idt = Tienda.objects.get(idTi=idTienda)
    return render(request, "admin_dash/admin_nuevo_producto.html",{'idt':idt,'tipo':tipo})

@login_required(login_url='login')
def nuevo_registro(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    imgsave = request.FILES['imagenProd'],
    idTi = request.POST['idTi_id'],
    tienda = int(str(idTi[0]))
    nombre = request.POST['nombreProd'],
    descripcion= request.POST['descripcionProd'],
    cat = request.POST['categoriaProd'],
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
    prod = Producto(nombreProd= str(nombre[0]), categoriaProd= str(cat[0]), imagenProd="productos/"+str(imgsave[0]),
                    marcaProd=str(marca[0]), descripcionProd=str(descripcion[0]), precioProd=float(precio[0]), 
                    medidasProd=str(medidas[0]), existenciasProd= existencias, idTi_id=tienda)
    
    #guarda objeto en la bd
    prod.save()
    #redirecciona a la pagina
    listaP = Producto.objects.filter(Q(idTi_id=tienda)&Q(estado=1))
    print(tienda)
    return render(request, "admin_dash/admin_productos.html",{'productos':listaP,'tipo':tipo})

@login_required(login_url='login')
def actualizacion_producto(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
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
    return render(request, "admin_dash/admin_productos.html",{'productos':listaP,'tipo':tipo})

@login_required(login_url='login')
def producto_eliminado(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    idp= request.POST['idProd']
    cambio = 0
    pr = Producto.objects.filter( idProd=idp ).update(estado=cambio)

    listaP = Producto.objects.filter(Q(idTi_id=idTienda) & Q(estado=1))
    print ("dato= "+ str(id))
    return render(request,"admin_dash/admin_productos.html",{'productos':listaP,'tipo':tipo})

@login_required(login_url='login')
def admin_solicitudes_vendedor(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    print("ID_USER:" + str(idAdmin))
    solicitudes = SolicitudesVendedor.objects.filter(noadmin=idAdmin).values('idSolVen','nombreV','correoV','direccionV','edadVen','status','idTi_id','idTi_id__nombreTi')#consulta de campos con inner join idTi__nombreTi es de la tabla de tiendas
    return render(request, "admin_dash/admin_solicitudes_vendedor.html",{'solicitudes':solicitudes,'tipo':tipo})

@login_required(login_url='login')
def admin_detalle_solicitud(request,idSolVen):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    solicitud = SolicitudesVendedor.objects.get(idSolVen=idSolVen)
    return render(request, "admin_dash/admin_detalle_solicitud.html",{'solicitud':solicitud,'tipo':tipo})

@login_required(login_url='login')
def cambiar_status_solicitud(request,idSolVen):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    cambio = 1
    sol = SolicitudesVendedor.objects.filter(idSolVen=idSolVen).update(status=cambio)
    
    #datos creacion catalogo
    solicitud = SolicitudesVendedor.objects.get(idSolVen=idSolVen)
    categoria = "Computo",
    status_nuevo = 1
    idVendedor = int(str(solicitud.idVen_id))
    idTienda = solicitud.idTi_id
    #creacion catalogo
    catalogo = Catalogo(categoria=categoria,status=status_nuevo,idVen_id=idVendedor,idTien_id=idTienda).save()
    #regresar a lista
    solicitudes = SolicitudesVendedor.objects.filter(noadmin=idAdmin).values('idSolVen','nombreV','correoV','direccionV','edadVen','status','idTi_id','idTi_id__nombreTi')

    return render(request, "admin_dash/admin_solicitudes_vendedor.html",{'solicitudes':solicitudes,'tipo':tipo})

@login_required(login_url='login')
def admin_rechazo_solicitud(request):
    return render(request, "admin_dash/admin_rechazo_solicitud.html")

@login_required(login_url='login')
def config_admin(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    #print ("id del admin es: " +  str(idAdmin))
    datos_admin = Administrador.objects.get(idUser_id=userid)
    print("ID_USUARIO: ", str(userid)) 
    print ("ID_ADMIN: " + str(idAdmin))
    return render(request, "admin_dash/config_admin.html",{'datos':datos_admin,'tipo':tipo})

@login_required(login_url='login')
def update_config(request):
    userid = request.user.id
    tipo = Usuario_Tipo.objects.get(idUser_id=userid)
    nombre = request.POST['nombreAdmin'],
    direccion = request.POST['direccionAdmin'],
    telefono = request.POST['telefonoAdmin'],
    correo = request.POST['correoAdmin']
    telefono = int(str(telefono[0]))
    # Objeto del modelo
    config = Administrador.objects.filter(idUser_id = idAdmin).update(nombreAdmin=str(nombre[0]),direccionAdmin=str(direccion[0]),
                                          telefonoAdmin=telefono,correoAdmin=str(correo))
    datos_admin = Administrador.objects.get(id=idAdmin)
    return render(request, "admin_dash/config_admin.html",{'datos':datos_admin,'tipo':tipo})
