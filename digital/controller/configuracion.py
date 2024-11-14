import json
import digital.modelos.configuracion_model as configuracion_model 
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def CONFObtenerGenerosFiltros(request) :  
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    resultado = configuracion_model.CONFObtenerGenerosFiltros()

    return JsonResponse(resultado, safe=False)