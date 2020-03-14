from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo (request):#Primera vista

    p1=Persona("Carlos","Sepulveda")
    ahora=datetime.datetime.now()
    temas=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    return render(request, "miplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas} )

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "cursoC.html",{"dameFecha":fecha_actual})

def cursoCss(request):
    fecha_actual=datetime.datetime.now()
    return render(request, "cursoCss.html",{"dameFecha":fecha_actual})


def despedida(request):#segunda vista
    return HttpResponse("hasta luego")

def dameFecha(request):#muestra Fecha
    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" %fecha_actual
    
    return HttpResponse(documento)

def calcularEdad(request,edad, anio):

    periodo=anio-2020
    edadfutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(anio,edadfutura)

    return HttpResponse(documento)

    