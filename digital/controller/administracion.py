import json
import digital.modelos.administracion_model as administracion_model 
import digital.controller.tokens as tokens
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ADMObtenerLibros(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :  ESTE ERA ANTES DE DIVIDIRLO
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerLibros()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerAutoresActivos(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerAutoresActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerAutores(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerAutores()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerEditoriales(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerEditoriales()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMAgregarEditorial(request) :
   # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMAgregarEditorial(datosGenerales["nombre"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarEditorial(request) :
   # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMHabilitarEditorial(datosGenerales["idEditorial"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDesHabilitarEditorial(request) :
   # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMDesHabilitarEditorial(datosGenerales["idEditorial"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerGenerosActivos(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerGenerosActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerGeneros(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerGeneros()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDesHabilitarGenero(request) :
   # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMDesHabilitarGenero(datosGenerales["idGenero"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarGenero(request) :
   # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMHabilitarGenero(datosGenerales["idGenero"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerEditorialesActivos(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerEditorialesActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerIdiomasActivos(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerIdiomasActivos()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMAgregarLibroCatalogo(request) :
    portada = request.FILES.get('portada')
    if not portada:
        return JsonResponse({'error': 'No se proporcionó la portada'}, status=400)

    # Guarda la portada
    ruta_portada = default_storage.save(f'portadas/{portada.name}', portada)

    # Captura los demás datos del formulario
    titulo = request.POST.get('titulo')
    precio = request.POST.get('precio')
    descuento = request.POST.get('descuento')
    iva = request.POST.get('iva')
    idGenero = request.POST.get('idGenero')
    sinopsis = request.POST.get('sinopsis')
    paginas = request.POST.get('paginas')
    idIdioma = request.POST.get('idIdioma')
    idEditorial = request.POST.get('idEditorial')
    fechaPublicacion = request.POST.get('fechaPublicacion')
    idAutor = request.POST.get('idAutor')
    isbn = request.POST.get('ISBN')

    nuevosDatosGenerales = {}
    nuevosDatosGenerales["titulo"] = titulo
    nuevosDatosGenerales["precio"] = precio
    nuevosDatosGenerales["descuento"] = descuento
    nuevosDatosGenerales["iva"] = iva
    nuevosDatosGenerales["idGenero"] = idGenero
    nuevosDatosGenerales["sinopsis"] = sinopsis
    nuevosDatosGenerales["paginas"] = paginas
    nuevosDatosGenerales["idIdioma"] = idIdioma
    nuevosDatosGenerales["idEditorial"] = idEditorial
    nuevosDatosGenerales["portada"] = ruta_portada
    nuevosDatosGenerales["fechaPublicacion"] = fechaPublicacion
    nuevosDatosGenerales["idAutor"] = idAutor
    nuevosDatosGenerales["ISBN"] = isbn
    nuevosDatosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")

    # resultado = administracion_model.ADMAgregarLibroCatalogo(datosGenerales)
    resultado = administracion_model.ADMAgregarLibroCatalogo(nuevosDatosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObenerLibroEdicion(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMObenerLibroEdicion(datosGenerales["idLibro"])
    # resultado["datosGenerales"] = administracion_model.ADMObenerLibroEdicion(datosGenerales["idLibro"])
    # resultado["autores"] = administracion_model.ADMObtenerAutoresLibro(datosGenerales["idLibro"])
    
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarLibro(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMDeshabilitarLibro(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarLibro(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMHabilitarLibro(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMEditarLibroCatalogo(request) :
    idLibro = request.POST.get('idLibro')
    portada = request.FILES.get('portada')
    rutaPortadaVieja = administracion_model.obtenerPortadaVieja(idLibro)
    if portada:
        default_storage.delete(rutaPortadaVieja)
        ruta_portada = default_storage.save(f'portadas/{portada.name}', portada)


    # Captura los demás datos del formulario
    titulo = request.POST.get('titulo')
    precio = request.POST.get('precio')
    descuento = request.POST.get('descuento')
    iva = request.POST.get('iva')
    idGenero = request.POST.get('idGenero')
    sinopsis = request.POST.get('sinopsis')
    paginas = request.POST.get('paginas')
    idIdioma = request.POST.get('idIdioma')
    idEditorial = request.POST.get('idEditorial')
    fechaPublicacion = request.POST.get('fechaPublicacion')
    idAutor = request.POST.get('idAutor')
    isbn = request.POST.get('ISBN')

    nuevosDatosGenerales = {}
    nuevosDatosGenerales["idLibro"] = idLibro
    nuevosDatosGenerales["titulo"] = titulo
    nuevosDatosGenerales["precio"] = precio
    nuevosDatosGenerales["descuento"] = descuento
    nuevosDatosGenerales["iva"] = iva
    nuevosDatosGenerales["idGenero"] = idGenero
    nuevosDatosGenerales["sinopsis"] = sinopsis
    nuevosDatosGenerales["paginas"] = paginas
    nuevosDatosGenerales["idIdioma"] = idIdioma
    nuevosDatosGenerales["idEditorial"] = idEditorial
    nuevosDatosGenerales["portada"] = ruta_portada
    nuevosDatosGenerales["fechaPublicacion"] = fechaPublicacion
    nuevosDatosGenerales["idAutor"] = idAutor
    nuevosDatosGenerales["ISBN"] = isbn

    resultado = administracion_model.ADMEditarLibroCatalogo(nuevosDatosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarAutor(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMDeshabilitarAutor(datosGenerales["idAutor"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarAutor(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]

    resultado = administracion_model.ADMHabilitarAutor(datosGenerales["idAutor"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerNacionesActivas(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerNacionesActivas()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMAgregarAutor(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    datosGenerales["fecha"] = datetime.now().strftime("%Y-%m-%d")

    resultado = administracion_model.ADMAgregarAutor(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerInventarioLibros(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)
    
    resultado = administracion_model.ADMObtenerInventarioLibros()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMModificarInventarioLibro(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMModificarInventarioLibro(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerDatosInventarioLibro(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMObtenerDatosInventarioLibro(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarInventario(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMHabilitarInventario(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarInventario(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMDeshabilitarInventario(datosGenerales["idLibro"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerVentas(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)
    
    resultado = administracion_model.ADMObtenerVentas()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerVenta(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMObtenerVenta(datosGenerales["idVenta"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMEntregarVenta(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMEntregarVenta(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMObtenerEmpleados(request) :
    # if(not request.session.get('idUsuario', False) or not request.sesion.get('idTipoUsuario', False)) :
    #     return HttpResponse()
    
    data = json.loads(request.body)
    datosGenerales = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGenerales)) :
        return JsonResponse(False, safe=False)

    resultado = administracion_model.ADMObtenerEmpleados()
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMRegistrarEmpleado(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    datosGenerales["activo"] = "S"
    datosGenerales["fechaRegistro"] = datetime.now().strftime("%Y-%m-%d")
    
    resultado = administracion_model.ADMRegistrarEmpleado(datosGenerales)
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMDeshabilitarEmpleado(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMDeshabilitarEmpleado(datosGenerales["idEmpleado"])
    return JsonResponse(resultado, safe=False)

@csrf_exempt
def ADMHabilitarEmpleado(request) :
    # if(not request.session.get('idUsuario', False)) :
    #     return HttpResponse()
    data = json.loads(request.body)
    datosGeneralesConToken = data.get("datosGenerales")
    if (not tokens.validarTokenEmpleados(datosGeneralesConToken["token"])) :
        return JsonResponse(False, safe=False)
    
    datosGenerales = datosGeneralesConToken["datosGenerales"]
    
    resultado = administracion_model.ADMHabilitarEmpleado(datosGenerales["idEmpleado"])
    return JsonResponse(resultado, safe=False)