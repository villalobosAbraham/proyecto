from digital.models import LogUsuarios
from django.db import transaction, IntegrityError, connection

def LOGIniciarSesion(datosGenerales) :
    try:
        usuario = LogUsuarios.objects.filter(
                email=datosGenerales["correo"], 
                contraseña=datosGenerales["contraseña"], 
                activo='S'
            ).values(
                'id', 
                'idtipousuario'
            ).first()
        return usuario
    except LogUsuarios.DoesNotExist:
        # Aquí puedes retornar None, un mensaje, o lanzar un error
        return False
    
def LOGRegistrarUsuario(datosGenerales) :
    try:
        with transaction.atomic():
            nuevo_usuario = LogUsuarios(
                email = datosGenerales["email"],
                contraseña = datosGenerales["contraseña"],
                nombre = datosGenerales["nombre"],
                apellidopaterno = datosGenerales["apellidopaterno"],
                apellidomaterno = datosGenerales["apellidomaterno"],
                fecharegistro = datosGenerales["fecharegistro"],
                telefono = datosGenerales["telefono"],
                fechanacimiento = datosGenerales["fechanacimiento"],
                activo = datosGenerales["activo"],
            )
            nuevo_usuario.save()
            # Otros posibles inserts o actualizaciones dentro de la misma transacción
        return True
    except IntegrityError as e:
        # Manejar la excepción, por ejemplo, loggear el error o retornar un mensaje
        print("Error en la Creacion de Usuario:", e)
        return False

def LOGObtenerUsuarioBarra(idUsuario) :
    sql = """SELECT
                    nombre, apellidopaterno, apellidomaterno, email, telefono, fechanacimiento
                FROM
                    log_usuarios
                WHERE
                    id = '""" + str(idUsuario) + """'"""
                    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultado = cursor.fetchone()
    
    if not resultado :
        return False
    else :
        return resultado
    
def LOGGuardarInformacionUsuarioBarra(datosGenerales, idUsuario) :
    try:
        with transaction.atomic():
            LogUsuarios.objects.filter(
                idusuario = idUsuario  
            ).update(
                email = datosGenerales["email"],
                contraseña = datosGenerales["contraseña"],
                nombre = datosGenerales["nombre"],
                apellidopaterno = datosGenerales["apellidopaterno"],
                apellidomaterno = datosGenerales["apellidomaterno"],
                telefono = datosGenerales["telefono"],
                fechanacimiento = datosGenerales["fechanacimiento"],
            )
            # Otros posibles inserts o actualizaciones dentro de la misma transacción
        return True
    except LogUsuarios.DoesNotExist:
        return False