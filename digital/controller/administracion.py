import json
import digital.modelos.administracion_model as administracion_model 
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

def ADMObtenerLibros(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()

    resultado = administracion_model.ADMObtenerLibros()
    return JsonResponse(resultado, safe=False)

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
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")

    resultado = administracion_model.ADMAgregarAutor(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerInventarioLibros(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    resultado = administracion_model.ADMObtenerInventarioLibros()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMModificarInventarioLibro(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = administracion_model.ADMModificarInventarioLibro(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerDatosInventarioLibro(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = administracion_model.ADMObtenerDatosInventarioLibro(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarInventario(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = administracion_model.ADMHabilitarInventario(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarInventario(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = administracion_model.ADMDeshabilitarInventario(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerVentas(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    resultado = administracion_model.ADMObtenerVentas()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerVenta(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = administracion_model.ADMObtenerVenta(datosGenerales["idVenta"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMEntregarVenta(request) :
    if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["idUsuario"] = request.session.get('idUsuario')
    
    resultado = administracion_model.ADMEntregarVenta(datosGenerales)
    return JsonResponse(resultado, safe=False)