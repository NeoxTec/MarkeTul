from django.views.generic.base import TemplateView
from django.shortcuts import render
from admin_dash.models import Producto,Tienda,Administrador
from vendedor.models import Vendedor,Catalogo, CatalogoProducto
# Create your views here.

"""Tienda"""

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
    catalogo_producto = CatalogoProducto(idProducto_id=idProd).save()
    listaC = Catalogo.objects.all()
    context = {'catalogos': listaC}
    return render(request, "vendedor/catalogos_vendedor.html", context)

def carrito(request):
    return render(request, "tienda/carrito.html")

def detalle_producto(request):
    return render(request, "tienda/detalle_producto.html")

def configuracion_cuenta(request):
    return render(request, "tienda/configuracion_cuenta.html")

def categoria_computo(request):
    listaCv = Catalogo.objects.all()
    context = {'catalogos': listaCv}
    return render(request, "tienda/categoria_computo.html", context)

def catalogos(request, idCatal):
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
    catalogo = Catalogo.objects.get(idCatal=idCatal)
    return render(request, "tienda/catalogos.html", {'productos':productos,'catalogo':catalogo})

def categorias(request):
    return render(request, "tienda/categorias.html")

def post_direccion(request):
    calle = request.POST['calle'],
    colonia = request.POST['colonia'],
    codigoPostal = request.POST['codigoPostal'],
    numExterior = request.POST['numeroExterior'],
    numInterior = request.POST['numeroInterior']
    #crea objeto
    dire = Direccion(calle = str(calle[0]), colonia= str(colonia[0]),
                    codigoPostal=str(codigoPostal[0]), numeroExterior=str(numExterior[0]),  
                    numeroInterior=str(numInterior[0]))
    
    #guarda objeto en la bd
    dire.save()
    #redirecciona a la pagina
    return render(request,"tienda/direccion_envio.html")

def direccion_envio(request):
    return render(request, "tienda/direccion_envio.html")

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

