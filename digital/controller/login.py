import json
import digital.modelos.login_model as login_model 
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.utils import timezone
import digital.controller.tokens as tokens

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("<h1>HOLA <h1>")

@csrf_exempt
def LOGIniciarSesion(request):
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = login_model.LOGIniciarSesion(datosGenerales)
    
    if (resultado) :
        request.session["idUsuario"] = resultado["id"]
        request.session["idTipoUsuario"] = resultado["idtipousuario"]

        token = tokens.crearToken(resultado["id"], resultado["idtipousuario"], datosGenerales["correo"], datosGenerales["contraseña"])

        return JsonResponse(token, safe=False)
    else :
        return JsonResponse(False, safe=False)

@csrf_exempt
def LOGRegistrarUsuario(request):
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = login_model.LOGRegistrarUsuario(datosGenerales)
    
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def LOGObtenerUsuarioBarra(request):
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarToken(datosGenerales)) :
        return JsonResponse(False, safe=False)
    
    resultado = login_model.LOGObtenerUsuarioBarra(datosGenerales["idUsuario"])
    
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def LOGGuardarInformacionUsuarioBarra(request):
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    idUsuario = request.session.get('idUsuario')
    
    resultado = login_model.LOGGuardarInformacionUsuarioBarra(datosGenerales, idUsuario)
    
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def LOGCerrarSesion(request):
    try:
        request.session.clear()
        request.session.flush()

        resultado = True
    except Exception as e:
        resultado = False
        print("Error al cerrar la sesión:", e)

    return JsonResponse(resultado, safe=False)