from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Acceso a las paginas del sitio
def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#Acceso a los libros
def libros(request):
    return render(request, 'libros/index.html')
def crear(request):
    return render(request, 'libros/crear.html')
