"""marketul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web import views as web_views

urlpatterns = [
    # Paths de admin_dash
    path('', include('admin_dash.urls')),

    # Paths de vendedor
    path('', include('vendedor.urls')),

    # Paths de vendedor
    path('', include('web.urls')),
    
    # Paths de Tienda
    path('', include('tienda.urls')),
    
    path('admin/', admin.site.urls),

]
