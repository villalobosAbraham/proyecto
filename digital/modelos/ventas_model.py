from django.db.models import Max, F
from django.db import transaction, IntegrityError, connection
import psycopg2
from psycopg2.extras import DictCursor
import digital.modelos.inventario_model as inventario_model 


def VENRegistrarVenta(datosGenerales) :
    diferencia = comprobarCantidadLibrosCarritoInventario(datosGenerales["idUsuario"])
    # librosVenta = obtenerLbrosCarritoVenta(datosGenerales["idUsuario"])
    


def comprobarCantidadLibrosCarritoInventario(idUsuario) :
    sql = """SELECT
                ven_carrodecompra.id
            FROM
                ven_carrodecompra
            LEFT JOIN 
                inv_inventariolibros ON ven_carrodecompra.idlibro = inv_inventariolibros.idlibro
            WHERE
                ven_carrodecompra.idusuario = '""" + str(idUsuario) + """' AND
                ven_carrodecompra.cantidad > inv_inventariolibros.cantidad AND
                ven_carrodecompra.activo = 'S'"""
    
    with connection.cursor() as cursor:
            cursor.execute(sql)
            resultado = cursor.fetchall()
    
    if not resultado :
        return True
    else :
        return False

# def comprobarDiferenciaCarritoInventario(idUsuario) :
#     sql = """SELECT
#                 ven_carrodecompra.idusuario, ven_carrodecompra.idlibro, ven_carrodecompra.cantidad,

#                 inv_inventariolibros.cantidad AS stock
#             FROM
#                 ven_carrodecompra
#             LEFT JOIN 
#                 inv_inventariolibros ON ven_carrodecompra.idlibro = inv_inventariolibros.idlibro
#             WHERE
#                 ven_carrodecompra.idusuario = '""" + str(idUsuario) + """' AND
#                 ven_carrodecompra.cantidad > inv_inventariolibros.cantidad AND
#                 ven_carrodecompra.activo = 'S'"""
    
#     with connection.cursor() as cursor:
#             cursor.execute(sql)
#             resultado = cursor.fetchall()
    
#     return resultado