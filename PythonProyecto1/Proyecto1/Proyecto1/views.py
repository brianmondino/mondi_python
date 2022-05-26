from asyncore import read
from datetime import datetime
from pipes import Template
#from re import template
from xml.dom.expatbuilder import DOCUMENT_NODE
from django.http import HttpResponse
from django.template import Template, context
from django.shortcuts import render

def saludo(request):
	return HttpResponse('Hola Django - Coder')

def segunda_vista(request):
	return HttpResponse('<br><br>Ya entendimos esto, es muy simple :)')

def diaDeHoy(request):
	dia = datetime.now()
	documentoDeTexto = f'Hoy es día: <br>{dia}'
	return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
	documentoDeTexto = f'Mi nombre es: <br><br>{nombre}'
	return HttpResponse(documentoDeTexto)

def calcNac (self, edad):
	cuenta = 2022 - edad
	calculo = f'Mi año de nac es:<br>{cuenta}'
	return HttpResponse(calculo)

def probando_template(request):
	return render(request,'template1.html', context={})


'''def probandoTemplate(self):
	miHtml = open ('template1.html')
	plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1
	#OJO importar template y contex, con: from Django.template importe Template, Context
	miHtml.close() #Cerramos el archivo
	miContexto = Context() #En este caso no hay nada ya que no hay parametros, IGUAL hay que hacerlo
	documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
	return HttpResponse(documento)'''