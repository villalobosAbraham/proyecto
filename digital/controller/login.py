import json
import digital.modelos.login_model as login_model 
from django.http import JsonResponse
from django.http import HttpResponse
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
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def LOGRegistrarUsuario(request):
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    
    resultado = login_model.LOGRegistrarUsuario(datosGenerales)
    
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def LOGObtenerUsuarioBarra(request):
    idUsuario = request.session.get('idUsuario')
    
    resultado = login_model.LOGObtenerUsuarioBarra(idUsuario)
    
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