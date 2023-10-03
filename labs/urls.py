"""
URL configuration for labs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from core import views as core_views 
from laboratorio import views as laboratorio_views
from laboratorio.views import insertar_laboratorio, editar_laboratorio, eliminar_laboratorio 

urlpatterns = [
    path('', core_views.home, name='home'),
    path('read_labs/', laboratorio_views.read_labs, name='read_labs'),
    path('create_labs/', insertar_laboratorio, name='create_labs'),
    path('update_labs/<int:laboratorio_id>/', editar_laboratorio, name='update_labs'),
    path('delete_labs/<int:laboratorio_id>/', eliminar_laboratorio, name='delete_labs'),
    path('admin/', admin.site.urls),
]
