import json
import digital.modelos.inventario_model as inventario_model 
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def INVObtenerLibrosPopulares(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    resultado = inventario_model.INVObtenerLibrosPopulares()

    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVObtenerLibrosRecomendados(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    resultado = inventario_model.INVObtenerLibrosRecomendados(1)

    return JsonResponse(resultado, safe=False)

@csrf_exempt
def INVAgregarAumentarLibroCarrito(request) :  #Falta hacer pruebas
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["idUsuario"] = request.session.get('idUsuario', 1)
    resultado = inventario_model.INVAgregarAumentarLibroCarrito(datosGenerales)

    return JsonResponse(resultado, safe=False)

