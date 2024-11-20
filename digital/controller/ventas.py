import json
import digital.modelos.ventas_model as ventas_model 
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def VENRegistrarVenta(request) :
    if(not request.session.get('idUsuario', False)) :
        return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    datosGenerales["idUsuario"] = request.session.get('idUsuario')
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")
    datosGenerales["hora"] = datetime.now().strftime('%H:%M:%S')

    resultado = ventas_model.VENRegistrarVenta(datosGenerales)
    return JsonResponse(resultado, safe=False)