from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

class Persona(object):
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo (request):#Primera vista

    p1=Persona("Carlos","Sepulveda")

    ahora=datetime.datetime.now()

    #doc_externo=open("C:/Users/carlo/Desktop/proyectoDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()

    doc_externo=loader.get_template('miplantilla.html')
    temas=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #context=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas})
    documento=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "momento_actual":ahora,"temas":temas})

    return HttpResponse(documento)

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

    