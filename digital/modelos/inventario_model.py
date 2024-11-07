from django.db.models import Max, F
from django.db import transaction, IntegrityError, connection
import psycopg2
from psycopg2.extras import DictCursor

def INVObtenerLibrosPopulares() :
    idsLibrosPopulares = obtenerIdsLibrosPopulares()


    return idsLibrosPopulares

def obtenerIdsLibrosPopulares() :
    sql = """SELECT id
            FROM (
                SELECT 
                    inv_visualizaciones.id, inv_visualizaciones.fecha
                FROM 
                    inv_visualizaciones
                JOIN
                    cat_libros ON inv_visualizaciones.idlibro = cat_libros.id
                LEFT JOIN
                    inv_inventariolibros ON inv_visualizaciones.idlibro = inv_inventariolibros.idlibro
                WHERE
                    cat_libros.activo = 'S' AND
                    inv_inventariolibros.cantidad > 0 AND
                    inv_inventariolibros.cantidad IS NOT NULL
                ORDER BY 
                    fecha DESC
            ) as subquery
            GROUP BY id
            ORDER BY MAX(fecha) DESC
            LIMIT 10 """
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return [{"id" : resultado[0]} for resultado in resultados]