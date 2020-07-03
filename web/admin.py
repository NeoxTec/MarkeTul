from django.contrib import admin
from admin_dash.models import Tienda,Producto,Administrador
# Register your models here.
admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(Administrador)
