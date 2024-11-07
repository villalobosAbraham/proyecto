import json
import digital.modelos.inventario_model as inventario_model 
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def INVObtenerLibrosPopulares(request) :
    resultado = inventario_model.INVObtenerLibrosPopulares()

    return JsonResponse(resultado, safe=False)