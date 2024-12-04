import json
import digital.modelos.inventario_model as inventario_model
import digital.controller.tokens as tokens 
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def INVObtenerLibrosPopulares(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarToken(datosGenerales)) :
        return JsonResponse(False, safe=False)
    
    resultado = inventario_model.INVObtenerLibrosPopulares()

    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVObtenerLibrosRecomendados(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarToken(datosGenerales)) :
        return JsonResponse(False, safe=False)
    
    resultado = inventario_model.INVObtenerLibrosRecomendados(1)

    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVComprobarCarritoCantidad(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarToken(datosGenerales)) :
        return JsonResponse(False, safe=False)
    
    resultado = inventario_model.INVComprobarCarritoCantidad(datosGenerales["idUsuario"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVAgregarAumentarLibroCarrito(request) :  #Falta hacer pruebas
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarToken(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    resultado = inventario_model.INVAgregarAumentarLibroCarrito(datosGenerales)

    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVObtenerLibrosCarritoCompra(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()

    resultado = inventario_model.INVObtenerLibrosCarritoCompra(request.session.get('idUsuario'))

    return JsonResponse(resultado, safe=False)
    
@csrf_exempt
def INVLimpiarCarritoCompra(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    resultado = inventario_model.INVLimpiarCarritoCompra(request.session.get('idUsuario'))
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVBorrarLibroCarrito(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["idUsuario"] = request.session.get('idUsuario')

    resultado = inventario_model.INVBorrarLibroCarrito(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVActualizarCantidadLibroCarrito(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["idUsuario"] = request.session.get('idUsuario')

    resultado = inventario_model.INVActualizarCantidadLibroCarrito(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVRegistrarVisualizacion(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["idUsuario"] = request.session.get('idUsuario')
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")

    resultado = inventario_model.INVRegistrarVisualizacion(datosGenerales)
    return JsonResponse(resultado, safe=False)