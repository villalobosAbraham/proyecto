from django.db.models import Max, F
from django.db import transaction, IntegrityError, connection

def CONFObtenerGenerosFiltros() :
    sql = """SELECT
                MAX(conf_genero.id) AS id,
                MAX(conf_genero.genero) AS genero,
                COUNT(inv_inventariolibros.cantidad) AS cantidad
            FROM
                conf_genero
            LEFT JOIN 
                cat_libros ON conf_genero.id = cat_libros.idgenero
            LEFT JOIN 
                inv_inventariolibros ON cat_libros.id = inv_inventariolibros.idlibro 
            WHERE
                conf_genero.activo = 'S'
            GROUP BY
                idgenero"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados