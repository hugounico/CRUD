from django.shortcuts import render, redirect
from .models import Laboratorio
from django.contrib.auth.decorators import login_required

# Create your views here.
def read_labs(request):     
    laboratorios = Laboratorio.objects.all()                             
    return render(request, 'laboratorio/read_labs.html', {'laboratorios': laboratorios})

# Crear Lab
@login_required
def insertar_laboratorio(request):
    if request.method == 'POST':
        lab_nombre = request.POST['lab_nombre']
        lab_ciudad = request.POST['lab_ciudad']
        lab_pais = request.POST['lab_pais']
        laboratorio = Laboratorio(nombre=lab_nombre, ciudad=lab_ciudad, pais=lab_pais)
        laboratorio.save()

        return redirect('/read_labs/')
    else:
        return render(request, 'laboratorio/create_labs.html')

# Editar Lab
@login_required    
def editar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(pk=laboratorio_id)

    if request.method == 'POST':
        lab_nombre = request.POST['lab_nombre']
        lab_ciudad = request.POST['lab_ciudad']
        lab_pais = request.POST['lab_pais']

        laboratorio.nombre = lab_nombre
        laboratorio.ciudad = lab_ciudad
        laboratorio.pais = lab_pais
        laboratorio.save()

        return redirect('/read_labs/')
    else:
        return render(request, 'laboratorio/update_labs.html', {'laboratorio': laboratorio})
    
# Eliminar Lab
@login_required
def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(pk=laboratorio_id)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('/read_labs/')

    return render(request, 'laboratorio/delete_labs.html', {'laboratorio': laboratorio})