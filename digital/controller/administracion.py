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

@csrf_exempt
def ADMObtenerAutoresActivos(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerAutoresActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerAutores(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerAutores()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerGenerosActivos(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerGenerosActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerEditorialesActivos(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerEditorialesActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerIdiomasActivos(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerIdiomasActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMAgregarLibroCatalogo(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")

    resultado = administracion_model.ADMAgregarLibroCatalogo(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarLibro(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")

    resultado = administracion_model.ADMDeshabilitarLibro(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarLibro(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")

    resultado = administracion_model.ADMHabilitarLibro(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarAutor(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")

    resultado = administracion_model.ADMDeshabilitarAutor(datosGenerales["idAutor"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarAutor(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")

    resultado = administracion_model.ADMHabilitarAutor(datosGenerales["idAutor"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerNacionesActivas(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerNacionesActivas()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMAgregarAutor(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")

    resultado = administracion_model.ADMAgregarAutor(datosGenerales)
    return JsonResponse(resultado, safe=False)