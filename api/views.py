from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import VentasSerializer,ConfigAdminSerializer, ConfigVendedorSerializer,VendedoresSerializer,ConfigConsumidorSerializer

from vendedor.models import Vendedor,SolicitudesVendedor, Ventas_vendedor,Catalogo,Vendedor
from admin_dash.models import Tienda,Administrador
from tienda.models import Consumidor

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