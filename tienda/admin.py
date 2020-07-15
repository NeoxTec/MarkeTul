from django.contrib import admin
from tienda.models import Compras , Forma_Pago, Cuenta, Direccion
# Register your models here.

admin.site.register(Compras)
admin.site.register(Forma_Pago)
from tienda.models import Cuenta,Direccion
# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Direccion)
