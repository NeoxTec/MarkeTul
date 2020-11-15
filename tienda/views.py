from django.views.generic.base import TemplateView
from django.shortcuts import render
from admin_dash.models import Producto,Tienda,Administrador
from vendedor.models import Vendedor,Catalogo, CatalogoProducto,Ventas_vendedor
from tienda.models import Consumidor,Carrito,Direccion,CarritoProducto, Compras, ProductoComprado, Forma_Pago
from django.contrib.auth.models import User
from registration.views import login,loginPage
from django.db.models import Q

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.

idCons = 0
idUser = 0
"""Tienda"""

@login_required(login_url='login')
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
        consumidor = Consumidor.objects.get(idUser_id=userid)
        ncarro = Carrito (cantidad=0,subtotal=0,idCons_id=consumidor.idConsumidor)
        ncarro.save()
    return render(request, "tienda/categorias.html")

@login_required(login_url='login')
def carrito_compras(request,idProd,idCatal):
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
    catalogo = Catalogo.objects.get(idCatal=idCatal)
    return render(request, "tienda/carrito_compras.html", {'productos':productos,'catalogo':catalogo})

@login_required(login_url='login')
def añadir_producto_carrito(request,idProd):
    # Obtiene el catalogo del producto
    catalogo_producto = CatalogoProducto.objects.get(idProducto_id=idProd)
    # Obtiene el producto
    producto = Producto.objects.get(idProd=idProd)
    # Id del catalogo del producto
    idCatProd = catalogo_producto.idCatalogo
    print("ID_CATALOGO:" + str(idCatProd.idCatal))
    # Obtiene el id del usuario
    userid = request.user.id
    # Obtiene los datos del perfil consumidor del usuario
    cons = Consumidor.objects.get(idUser_id=userid)
    # Obtiene el carrito del consumidor logueado
    carrito = Carrito.objects.get(idCons_id=cons.idConsumidor)
    # Obtiene la Cantidad del producto
    cantidad = request.POST['cantidad']
    # Covierte a entero la cantidad
    cantidad = int(cantidad)
    # Conteo de si ya se agrego el producto
    conteo = CarritoProducto.objects.filter(idProducto_id=idProd,idCatalogo_id=idCatProd.idCatal,idCarrito_id=carrito.idCarrito).count()
    print("Conteo: "+str(conteo))
    print("ID_CONS:" + str(cons.idConsumidor))
    if conteo == 1:
        prod_ag = CarritoProducto.objects.get(idProducto_id=idProd)
        cantidad_nueva = prod_ag.cantidad + cantidad
        actualizar = CarritoProducto.objects.filter(idProducto_id=idProd,idCarrito_id=carrito.idCarrito,idCatalogo=idCatProd.idCatal).update(cantidad=cantidad_nueva)
    else:
        carrito_producto = CarritoProducto (idCarrito_id=carrito.idCarrito,idCatalogo_id=idCatProd.idCatal,idProducto_id=idProd,cantidad=cantidad).save()
    
    listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
    productos = []
    subtotal = 0.0
    cantidad = 0
    print("CANTIDAD: " + str(cantidad))
    for producto in listaC:
        prod = Producto.objects.get(idProd=producto.idProducto_id)
        cantidad = cantidad + producto.cantidad
        if producto.cantidad > 1:
            subtotal= subtotal + (float(prod.precioProd)*producto.cantidad)
        else:
            subtotal = subtotal + float(prod.precioProd)
        
        productos.append(prod)
    print("SUBTOTAL: " + str(subtotal))
    actualizacion = Carrito.objects.filter(idCons_id=cons.idConsumidor).update(cantidad=cantidad,subtotal=subtotal)
    carro = Carrito.objects.get(idCons_id=cons.idConsumidor)
    context = {'productos':productos, 'carrito':carro, 'listaC':listaC}
    return render(request, "tienda/carrito.html",context)

@login_required(login_url='login')
def carrito(request):
    userid = request.user.id
    cons = Consumidor.objects.get(idUser_id=userid) 
    carrito = Carrito.objects.get(idCons_id=cons.idConsumidor)
    listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
    productos = []
    subtotal = 0.0
    cantidad = 0
    print("CANTIDAD: " + str(cantidad))
    for producto in listaC:
        prod = Producto.objects.get(idProd=producto.idProducto_id)
        cantidad = cantidad + producto.cantidad
        if producto.cantidad > 1:
            subtotal= subtotal + (float(prod.precioProd)*producto.cantidad)
        else:
            subtotal = subtotal + float(prod.precioProd)
        
        productos.append(prod)
    print("SUBTOTAL: " + str(subtotal))
    actualizacion = Carrito.objects.filter(idCons_id=cons.idConsumidor).update(cantidad=cantidad,subtotal=subtotal)
    carro = Carrito.objects.get(idCons_id=cons.idConsumidor)
    context = {'productos':productos, 'carrito':carro, 'listaC':listaC}
    return render(request, "tienda/carrito.html",context)

@login_required(login_url='login')
def eliminar_producto_carrito(request,idProd,idCarrito):
    userid = request.user.id
    cantidad_recuperada = request.POST['cantidad']
    cantidad_recuperada = int(cantidad_recuperada)
    cantidad_nueva = 0
    producto_eliminar = CarritoProducto.objects.get(idProducto_id=idProd)
    print("CARRITO:" + str(idCarrito))
    print("PRODUCTO: "+ str(idProd))

    if cantidad_recuperada < producto_eliminar.cantidad:

        cantidad_nueva = (producto_eliminar.cantidad - cantidad_recuperada)
        print("CANTIDAD_NUEVA: "+ str(cantidad_nueva))

        eliminar = CarritoProducto.objects.filter(idProducto_id=idProd,idCarrito_id=idCarrito).update(cantidad=cantidad_nueva)

    elif cantidad_recuperada == producto_eliminar.cantidad:
        
        eliminar = CarritoProducto.objects.filter(idProducto_id=idProd,idCarrito_id=idCarrito).delete()

    cons = Consumidor.objects.get(idUser_id=userid) 
    carrito = Carrito.objects.get(idCons_id=cons.idConsumidor)
    listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
    productos = []
    subtotal = 0.0
    cantidad = 0
    for producto in listaC:
        prod = Producto.objects.get(idProd=producto.idProducto_id)
        cantidad = cantidad + producto.cantidad
        if producto.cantidad > 1:
            subtotal= subtotal + (float(prod.precioProd)*producto.cantidad)
        else:
            subtotal = subtotal + float(prod.precioProd)
        productos.append(prod)
    print("SUBTOTAL: " + str(subtotal))
    actualizacion = Carrito.objects.filter(idCons_id=cons.idConsumidor).update(cantidad=cantidad,subtotal=subtotal)
    carro = Carrito.objects.get(idCons_id=cons.idConsumidor)
    context = {'productos':productos, 'carrito':carro, 'listaC':listaC}
    return render(request, "tienda/carrito.html",context)


@login_required(login_url='login')
def proceso_pago(request):
    userid = request.user.id
    cons = Consumidor.objects.get(idUser_id=userid) 
    carrito = Carrito.objects.get(idCons_id=cons.idConsumidor)
    listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
    productos = []
    for producto in listaC:
        prod = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(prod)
    context = {'productos':productos, 'carrito':carrito, 'listaC':listaC}
    return render(request, "tienda/proceso_pago.html",context)

@login_required(login_url='login')
def pago_exitoso(request):
    userid = request.user.id
    cons = Consumidor.objects.get(idUser_id=userid) 
    carrito = Carrito.objects.get(idCons_id=cons.idConsumidor)
    #conteo = Forma_Pago.objects.filter(idUser_id=userid).count()
    #forma = Forma_Pago.objects.get(idUser_id=userid)
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    total = int(carrito.subtotal)
    """if (conteo != 1):
        messages.warning(request, 'Error en el pago, agregue una forma de pago')
        userid = request.user.id
        datos_consumidor = Consumidor.objects.get(idUser_id=userid)
        return render(request, "tienda/forma_pago.html", {'datos':datos_consumidor})
    else:"""
    agregar_compras = Compras(idCons_id=datos_consumidor.idConsumidor,total=total).save()
    ultima_compra = Compras.objects.last()
    compra_nueva = Compras.objects.get(idCompra=ultima_compra.idCompra)
    listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
    for producto in listaC:
        cantidad = 0
        venta = 0.0
        prod = Producto.objects.get(idProd=producto.idProducto_id)
        comprado = ProductoComprado(idCompra_id=compra_nueva.idCompra,idProducto_id=prod.idProd,status=0).save()
        cantidad = cantidad + producto.cantidad
        venta = venta + (float(prod.precioProd)*producto.cantidad)
        ventas = Ventas_vendedor(idCatalogo_id=producto.idCatalogo_id,idProducto_id=producto.idProducto_id,cantidad=cantidad,venta=venta).save()
        existencias_up = prod.existenciasProd - cantidad
        descuento = Producto.objects.filter(idProd=producto.idProducto_id).update(existenciasProd=existencias_up)
        quitar = CarritoProducto.objects.filter(idProducto_id=prod.idProd).delete()
    conteo = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito).count()
    if (conteo != 1):
        actualizar = Carrito.objects.filter(idCons_id=cons.idConsumidor).update(cantidad=0,subtotal=0.0)
    messages.success(request, '¡Felicidades! Tu compra ha sido exitosa.')

    compras = Compras.objects.filter(idCons_id=datos_consumidor.idConsumidor)
    return render(request,"tienda/compras.html",{'datos':datos_consumidor,'compras':compras})

@login_required(login_url='login')
def detalle_producto(request):
    return render(request, "tienda/detalle_producto.html",context)

@login_required(login_url='login')
def compras(request):
    userid = request.user.id
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    compras = Compras.objects.filter(idCons_id=datos_consumidor.idConsumidor)
    return render(request, "tienda/compras.html",{'datos':datos_consumidor,'compras':compras})

@login_required(login_url='login')
def pedidos(request,idCompra):
    userid = request.user.id
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    pedidos = []
    productos = ProductoComprado.objects.filter(idCompra=idCompra)
    for producto in productos:
        pedido = Producto.objects.get(idProd=producto.idProducto_id)
        pedidos.append(pedido)
        print (pedidos)
    return render(request, "tienda/pedidos.html",{'datos':datos_consumidor,'pedidos':pedidos})

@login_required(login_url='login')
def configuracion_cuenta(request):
    userid = request.user.id # Se obtiene el id
    print("IDUSUARIO: "+str(userid))
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    return render(request, "tienda/configuracion_cuenta.html", {'datos':datos_consumidor}) 

@login_required(login_url='login')
def guardar_config_con(request):
    userid = request.user.id
    usuario = User.objects.get(id=userid)
    nombre = request.POST['nombre']
    correo = request.POST['correo']
    telefono = request.POST['telefono']
    nc = request.POST['nc']
    cc = request.POST['cc']
    configuracion = Consumidor.objects.filter(idUser_id = userid).update(nombre=str(nombre), telefono=int(str(telefono)), correo=str(correo))

    if nc and nc == cc:
        usuario.set_password(nc)
        usuario.save()
        messages.success(request,"Contraseña cambiada correctamente")
    elif nc and nc != cc:
        messages.error(request,"Contraseñas no coinciden")

    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    return render(request, "tienda/configuracion_cuenta.html", {'datos':datos_consumidor}) 

def categoria_computo(request):
    listaCv = Catalogo.objects.filter(categoria="Computo")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_computo.html", context)

def categoria_niño(request):
    listaCv = Catalogo.objects.filter(categoria="Niños")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_niño.html", context)

def categoria_hombre(request):
    listaCv = Catalogo.objects.filter(categoria="Hombre")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_hombre.html", context)

def categoria_mujer(request):
    listaCv = Catalogo.objects.filter(categoria="Mujer")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_mujer.html", context)

def categoria_libros(request):
    listaCv = Catalogo.objects.filter(categoria="Libros")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_libros.html", context)

def categoria_mascotas(request):
    listaCv = Catalogo.objects.filter(categoria="Mascotas")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_mascotas.html", context)

def categoria_muebles(request):
    listaCv = Catalogo.objects.filter(categoria="Muebles")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_muebles.html", context)

def categoria_electrodomesticos(request):
    listaCv = Catalogo.objects.filter(categoria="Electrodomesticos")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)       
    context = {'catalogos': listaCv,'vendedores': vendedores}
    return render(request, "tienda/categoria_electrodomesticos.html", context)

def catalogos(request, idCatal):
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
        print("URL:"+str(pro.imagenProd))
    catalogo = Catalogo.objects.get(idCatal=idCatal)
    vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
    return render(request, "tienda/catalogos.html", {'productos':productos,'catalogo':catalogo,'vendedor':vendedor})

@login_required(login_url='login')
def direccion_envio(request):
    userid = request.user.id # Se obtiene el id
    print("IDUSUARIO: "+str(userid))
    conteo = Direccion.objects.filter(idUser_id=userid).count()
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    if (conteo != 1):
        context = {'datos':datos_consumidor}
    else:
        direccion = Direccion.objects.get(idUser_id=userid)
        context = {'datos':datos_consumidor,'direccion':direccion}
    return render(request, "tienda/direccion_envio.html", context) 

@login_required(login_url='login')
def guardar_direccion(request):
    userid = request.user.id
    codigoPostal= request.POST['codigoPostal']
    calle = request.POST['calle']
    colonia = request.POST['colonia']
    numeroExterior = request.POST['numeroExterior']
    numeroInterior = request.POST['numeroInterior']
    
    direccion = Direccion.objects.filter(idUser_id = userid).update(codigoPostal=str(codigoPostal), calle=str(calle), colonia=str(colonia), 
    numeroExterior=str(numeroExterior),numeroInterior=str(numeroInterior))
    
    direccion = Direccion.objects.get(idUser_id=userid)
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    return render(request, "tienda/direccion_envio.html", {'datos':datos_consumidor,'direccion':direccion})

@login_required(login_url='login')
def post_forma_pago(request):
    userid = request.user.id
    conteo = Forma_Pago.objects.filter(idUser_id=userid).count()
    nombre_propietario = request.POST['nombre_propietario'],
    numero_tarjeta = request.POST['numero_tarjeta'],
    mes = request.POST['mes']
    anio = request.POST['anio']
    tipo = request.POST['tipo_pago']
    if conteo != 1:
        #crea objeto
        pago = Forma_Pago(nombre_propietario = str(nombre_propietario[0]), numero_tarjeta = str(numero_tarjeta[0]), 
        mes_vencimiento=str(mes),anio_vencimiento=str(anio), tipo_pago=str(tipo), idUser_id=userid)
        #guarda objeto en bd
        pago.save()
        #redirecciona a la pagina
    else:
        actualizar = Forma_Pago.objects.filter(idUser_id=userid).update(nombre_propietario = str(nombre_propietario[0]), numero_tarjeta = str(numero_tarjeta[0]), 
        mes_vencimiento=str(mes),anio_vencimiento=str(anio), tipo_pago=str(tipo))
        
    userid = request.user.id
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    info_pago = Forma_Pago.objects.get(idUser_id=userid)
    return render(request, "tienda/forma_pago.html", {'datos':datos_consumidor,'info':info_pago})
    
def direccion_envio1(request):
    return render(request, "tienda/direccion_envio1.html")

@login_required(login_url='login')
def forma_pago(request):
    userid = request.user.id
    datos_consumidor = Consumidor.objects.get(idUser_id=userid)
    info_pago = Forma_Pago.objects.get(idUser_id=userid)
    return render(request, "tienda/forma_pago.html", {'datos':datos_consumidor,'info':info_pago})

def pago_error(request):
    return render(request, "tienda/pago_error.html")



