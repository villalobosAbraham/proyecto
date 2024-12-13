import json
import digital.modelos.ventas_model as ventas_model 
import digital.controller.tokens as tokens
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def VENRegistrarVenta(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarToken(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")
    datosGenerales["hora"] = datetime.now().strftime('%H:%M:%S')

    resultado = ventas_model.VENRegistrarVenta(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def VENObtenerDetallesVenta(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarToken(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = ventas_model.VENObtenerDetallesVenta(datosGenerales["idVenta"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def VENObtenerVentasUsuario(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarToken(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = ventas_model.VENObtenerVentasUsuario(datosGenerales["idUsuario"])
    return JsonResponse(resultado, safe=False)