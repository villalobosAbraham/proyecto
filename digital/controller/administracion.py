import json
import digital.modelos.administracion_model as administracion_model 
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ADMObtenerLibros(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerLibros()
    return JsonResponse(resultado, safe=False)