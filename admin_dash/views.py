from django.shortcuts import render

# Create your views here.
""" Dashboard Administrador """

def admin_dash(request):
    return render(request, "admin_dash/admin_dash.html")

def vendedores(request):
    return render(request, "admin_dash/vendedores.html")

def admin_productos(request):
    return render(request, "admin_dash/admin_productos.html") 

def admin_detalle_producto(request):
    return render(request, "admin_dash/admin_detalle_producto.html")

def admin_nuevo_producto(request):
    return render(request, "admin_dash/admin_nuevo_producto.html") 

def admin_solicitudes_vendedor(request):
    return render(request, "admin_dash/admin_solicitudes_vendedor.html") 

def admin_detalle_solicitud(request):
    return render(request, "admin_dash/admin_detalle_solicitud.html") 

def admin_rechazo_solicitud(request):
    return render(request, "admin_dash/admin_rechazo_solicitud.html") 

def config_admin(request):
    return render(request, "admin_dash/config_admin.html") 