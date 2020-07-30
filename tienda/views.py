from django.views.generic.base import TemplateView
from django.shortcuts import render
from admin_dash.models import Producto,Tienda,Administrador
from vendedor.models import Vendedor,Catalogo, CatalogoProducto
from tienda.models import Consumidor,Carrito,Direccion
from django.contrib.auth.models import User
# Create your views here.

idCons = 0
idUser = 0
"""Tienda"""

def categorias(request):
    userid = request.user.id
    global idUser
    idUser = userid
    id_usuario = User.objects.get(id=userid)
    print("USUARIO_ID: "+str(userid))
    conteo = Consumidor.objects.filter(idUser_id=userid).count()
    if (conteo != 1):
        ncon = Consumidor (nombre=id_usuario.first_name,idUser_id=userid,correo=id_usuario.email)
        ncon.save()
    return render(request, "tienda/categorias.html")

def compras(request):
    return render(request, "tienda/compras.html")

def carrito_compras(request,idProd,idCatal):
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
    catalogo = Catalogo.objects.get(idCatal=idCatal)
    return render(request, "tienda/carrito_compras.html", {'productos':productos,'catalogo':catalogo})

def añadir_producto_carrito(request,idProd):
    catalogo_producto = CatalogoProducto.objects.get(idProducto_id=idProd)
    producto = Producto.objects.get(idProd=idProd)
    subtotal = float(producto.precioProd)
    conteo = Carrito.objects.all().count()
    idCatProd = int(catalogo_producto.idCatProd)

    if (conteo != 1):
        carrito = Carrito(cantidad=1,subtotal=subtotal,idCatProd_id=idCatProd,idProd_id=idProd).save()
    elif (conteo >= 1):
        carrito = Carrito.objects.get(idCatProd_id=idCatProd)
        idcarrito = carrito.idCarrito
        añadir = Carrito(cantidad=1,subtotal=subtotal,idCatProd_id=idCatProd,idProd_id=idProd).save().filter(idCarrito=idcarrito)
    return render(request, "tienda/categorias.html")

def carrito(request):
    carritos = Carrito.objects.all()
    for producto in carritos:
        prod = Producto.objects.get(idProd=producto.idProd_id)
    print(producto.idProd_id)
    carrito = Carrito.objects.get(idProd_id=producto.idProd_id)
    context = {'producto':prod, 'carrito':carrito}
    return render(request, "tienda/carrito.html",context)

def detalle_producto(request):
    return render(request, "tienda/detalle_producto.html")

def configuracion_cuenta(request):
    userid = request.user.id # Se obtiene el id
    print("IDUSUARIO: "+str(userid))
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    return render(request, "tienda/configuracion_cuenta.html", {'datos':datos_consumidor}) 

def guardar_config_con(request):
    userid = request.user.id
    nombre = request.POST['nombre']
    correo = request.POST['correo']
    telefono = request.POST['telefono']
    
    configuracion = Consumidor.objects.filter(idUser_id = userid).update(nombre=str(nombre), telefono=int(str(telefono)), correo=str(correo))
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    return render(request, "tienda/configuracion_cuenta.html", {'datos':datos_consumidor}) 

def categoria_computo(request):
    listaCv = Catalogo.objects.all()
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_computo.html", context)

def catalogos(request, idCatal):
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
    catalogo = Catalogo.objects.get(idCatal=idCatal)
    vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
    return render(request, "tienda/catalogos.html", {'productos':productos,'catalogo':catalogo,'vendedor':vendedor})

def direccion_envio(request):
    userid = request.user.id # Se obtiene el id
    print("IDUSUARIO: "+str(userid))
    datos_consumidor = Direccion.objects.get(idUser_id=userid)
    return render(request, "tienda/direccion_envio.html", {'datos':datos_consumidor}) 
   
def guardar_direccion(request):
    userid = request.user.id
    codigoPostal= request.POST['codigoPostal']
    calle = request.POST['calle']
    colonia = request.POST['colonia']
    numeroExterior = request.POST['numeroExterior']
    numeroInterior = request.POST['numeroInterior']
    
    direccion = Direccion.objects.filter(idUser_id = userid).update(codigoPostal=str(codigoPostal), calle=str(calle), colonia=str(colonia), 
    numeroExterior=str(numeroExterior),numeroInterior=str(numeroInterior))
    datos_consumidor = Direccion.objects.get(idUser_id=userid)
    return render(request, "tienda/direccion_envio.html", {'datos':datos_consumidor})

def post_forma_pago(request):
    nombre_propietario = request.POST['nombre_propietario'],
    numero_tarjeta = request.POST['numero_tarjeta'],
    fvencimiento = request.POST['fvencimiento']
    #crea objeto
    pago = Forma_Pago(nombre_propietario = str(nombre_propietario[0]), numero_tarjeta = str(numero_tarjeta[0]), 
    fvencimiento = str(fvencimiento[0]))

    #guarda objeto en bd
    pago.save()
    #redirecciona a la pagina
    return render(request,"tienda/forma_pago.html")
    
def direccion_envio1(request):
    return render(request, "tienda/direccion_envio1.html")

def forma_pago(request):
    return render(request, "tienda/forma_pago.html")

def proceso_pago(request):
    return render(request, "tienda/proceso_pago.html")

def pago_error(request):
    return render(request, "tienda/pago_error.html")

def pago_exitoso(request):
    return render(request, "tienda/pago_exitoso.html")

