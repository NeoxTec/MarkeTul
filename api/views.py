from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VentasSerializer,ConfigAdminSerializer, ConfigVendedorSerializer,VendedoresSerializer,ConfigConsumidorSerializer,Categoria_ComputoSerializer,CatalogoProductoSerializer,CarritoSerializer,CarritoProductoSerializer

from vendedor.models import Vendedor,SolicitudesVendedor, Ventas_vendedor,Catalogo,Vendedor,CatalogoProducto
from admin_dash.models import Tienda,Administrador,Producto
from tienda.models import Consumidor,Carrito,CarritoProducto

from django.conf import settings

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/ventas-list/',
        'Detail View':'/config-admin/',
        'List': '/vendedores/',
        'Detail View':'/consumidor-config/',
        'Detail View':'/vendedor-config/',
        'List':'/categoria-computo/',
        'List':'/catalogo-computo/<int:idCatal>/',
        'List':'/carrito/',
        'List':'/carrito-productos/',
        
    }
    return Response(api_urls)

@api_view(['GET'])
def ventasList(request):
    if settings.DEBUG:
        catalogos = Catalogo.objects.filter(idVen_id=4)
    else:
        catalogos = Catalogo.objects.filter(idVen_id=5)
    ventas = []
    for catalogo in catalogos:
        ventas_g = Ventas_vendedor.objects.filter(idCatalogo_id=catalogo.idCatal)
        for venta in ventas_g:
            ventas.append(venta)
    serializer = VentasSerializer(ventas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def config_admin(request):
    if settings.DEBUG:
        datos_admin = Administrador.objects.get(idUser_id=15)
    else: 
        datos_admin = Administrador.objects.get(idUser_id=18)
    serializer = ConfigAdminSerializer(datos_admin)
    return Response(serializer.data)

@api_view(['GET'])
def vendedores(request):
    if settings.DEBUG:
        datos_admin = Administrador.objects.get(idUser_id=15)
        tienda = Tienda.objects.get(idAdmin_id=datos_admin.id)
        solicitudes = SolicitudesVendedor.objects.filter(idTi_id=tienda.idTi)
    else: 
        datos_admin = Administrador.objects.get(idUser_id=18)
        tienda = Tienda.objects.get(idAdmin_id=datos_admin.id)
        solicitudes = SolicitudesVendedor.objects.filter(idTi_id=tienda.idTi)
    serializer = VendedoresSerializer(solicitudes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def vendedor_config(request):
    if settings.DEBUG:
        datos_vendedor = Vendedor.objects.get(idUser_id=16)
    else:
        datos_vendedor = Vendedor.objects.get(idUser_id=19)
    serializer = ConfigVendedorSerializer(datos_vendedor)
    return Response(serializer.data)

@api_view(['GET'])
def consumidor_config(request):
    if settings.DEBUG:
        datos_cons = Consumidor.objects.get(idUser_id=18)
    else:
        datos_cons = Consumidor.objects.get(idUser_id=20)
    serializer = ConfigConsumidorSerializer(datos_cons)
    return Response(serializer.data)

@api_view(['GET'])
def categoria_computo(request):
    listaCv = Catalogo.objects.filter(categoria="Computo")
    vendedores = []
    for catalogo in listaCv:
        vendedor = Vendedor.objects.get(idVend=catalogo.idVen_id)
        vendedores.append(vendedor)
    serializer = Categoria_ComputoSerializer(vendedores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def catalogo_productos(request,idCatal):
    listaP = CatalogoProducto.objects.filter(idCatalogo_id=idCatal)
    productos = []
    for producto in listaP:
        pro = Producto.objects.get(idProd=producto.idProducto_id)
        productos.append(pro)
    serializer = CatalogoProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def carrito(request):
    if settings.DEBUG:
        carrito = Carrito.objects.get(idCons_id=6)
    else:
        carrito = Carrito.objects.get(idCons_id=4)
    serializer = CarritoSerializer(carrito)
    return Response(serializer.data)

@api_view(['GET'])
def carrito_productos(request):
    if settings.DEBUG:
        carrito = Carrito.objects.get(idCons_id=6)
        listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
        productos = []
        for producto in listaC:
            prod = Producto.objects.get(idProd=producto.idProducto_id)
            productos.append(prod)
    else:
        carrito = Carrito.objects.get(idCons_id=4)
        listaC = CarritoProducto.objects.filter(idCarrito_id=carrito.idCarrito)
        productos = []
        for producto in listaC:
            prod = Producto.objects.get(idProd=producto.idProducto_id)
            productos.append(prod)
    serializer = CarritoProductoSerializer(productos, many=True)
    return Response(serializer.data)