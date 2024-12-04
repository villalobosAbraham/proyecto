import json
import digital.modelos.configuracion_model as configuracion_model 
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import digital.controller.tokens as tokens

@csrf_exempt
def CONFObtenerGenerosFiltros(request) :  
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarToken(datosGenerales)) :
        return JsonResponse(False, safe=False)
    resultado = configuracion_model.CONFObtenerGenerosFiltros()

    return JsonResponse(resultado, safe=False)

@csrf_exempt
def CONFFiltrarLibros(request) :  
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["generos"] = ",".join(map(str,datosGenerales["generos"]))
    
    resultado = configuracion_model.CONFFiltrarLibros(datosGenerales)

    return JsonResponse(resultado, safe=False)