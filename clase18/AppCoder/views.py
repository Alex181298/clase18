from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.
def crear_curso(request,camada):
    curso= Curso(nombre='Python', camada=camada)
    curso.save()
    
    return HttpResponse(f'Usted ha creado un curso! {camada}')
