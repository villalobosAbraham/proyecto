from datetime import datetime, timedelta
    

def crearToken(idUsuario, idTipoUsuario, correo, contraseña) :
    token = {}

    token["idUsuario"] = idUsuario
    token["idTipoUsuario"] = idTipoUsuario
    token["correo"] = correo
    token["contraseña"] = contraseña
    token["expiracion"] = crearHoraExpiracion()

    return token

def crearHoraExpiracion() :
    current_time = datetime.now()

    # Sumar 3 horas usando timedelta
    new_time = current_time + timedelta(hours=3)

    return new_time

def actualizarToken(token) :
    if not validarToken(token) :
        return False
    
    token["expiracion"] = crearHoraExpiracion()

    return token
    
def validarToken(token) :
    if not token :
        return False
    
    try :
        fechaActual = datetime.now()
        fechaToken = datetime.strptime(token["expiracion"], "%Y-%m-%dT%H:%M:%S.%fZ")

        if (fechaActual > fechaToken) :
            return False
        return True
    except :
        return False
    