from rest_framework import serializers
from vendedor.models import Vendedor,SolicitudesVendedor, Ventas_vendedor,Catalogo
from admin_dash.models import Tienda,Administrador, Producto
from tienda.models import Consumidor,Carrito,CarritoProducto

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas_vendedor
        fields = '__all__'  #['idVenta','cantidad','venta','idCatalogo_id','idProducto_id']

class ConfigAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

class ConfigVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudesVendedor
        fields = '__all__'

class ConfigConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidor
        fields = '__all__'

class Categoria_ComputoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class CatalogoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'

class CarritoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'