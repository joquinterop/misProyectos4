from django.shortcuts import render # type: ignore

from .models import Alumno,Genero
# Create your views here.

def index(request):
    alumnos= Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    alumnos = Alumno.objects.raw("SELECT * FROM alumnos_alumno")
    print(alumnos)
    context = {"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def lista_generos(request):
    generos = Genero.objects.all()
    context = {"generos":generos}
    return render(request,'alumnos/genero.html',context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request,'alumnos/alumnos_list.html',context)

def alumnosAdd(request):
    if request.method is not "POST":
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_add.html', context)
