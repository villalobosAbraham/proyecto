from django.db.models import Max, F
from django.db import transaction, IntegrityError, connection
import psycopg2
from psycopg2.extras import DictCursor

def INVObtenerLibrosPopulares() :
    idsLibrosPopulares = obtenerIdsLibrosPopulares()

    sql = """SELECT 
                cat_libros.id AS idlibro,
                MAX(cat_libros.titulo) AS titulo,
                MAX(cat_libros.precio) AS precio,
                MAX(cat_libros.descuento) AS descuento,
                MAX(cat_libros.iva) AS iva,
                MAX(cat_libros.idgenero) AS idgenero,
                MAX(cat_libros.fechapublicacion) AS fechapublicacion,
                MAX(cat_libros.portada) AS portada,
                MAX(cat_libros.sinopsis) AS sinopsis,
                MAX(cat_libros.paginas) AS paginas,
                
                MAX(conf_genero.genero) AS genero,
                MAX(cat_idioma.idioma) AS idioma,
                MAX(cat_editoriales.editorial) AS editorial,
                
                STRING_AGG(CONCAT(conf_autores.nombre, ' ', conf_autores.apellidopaterno, ' ', conf_autores.apellidomaterno), '  ') AS autores,
                MAX(inv_inventariolibros.cantidad) AS limiteLibro
            FROM 
                cat_libros 
            LEFT JOIN 
                conf_genero ON cat_libros.idgenero = conf_genero.id
            LEFT JOIN 
                cat_idioma ON cat_libros.ididioma = cat_idioma.id
            LEFT JOIN 
                cat_editoriales ON cat_libros.ideditorial = cat_editoriales.id
            LEFT JOIN
                inv_inventariolibros ON cat_libros.id = inv_inventariolibros.idlibro
            LEFT JOIN 
                cat_librosautores ON cat_libros.id = cat_librosautores.idlibro
            LEFT JOIN 
                conf_autores ON cat_librosautores.idautor = conf_autores.idautor
            WHERE 
                cat_libros.id = ANY(%s) AND
                cat_libros.activo = 'S'
            GROUP BY
                cat_libros.id"""
    with connection.cursor() as cursor:
        cursor.execute(sql, [idsLibrosPopulares])
        resultados = cursor.fetchall()

    return resultados

def obtenerIdsLibrosPopulares():
    sql = """SELECT idlibro
        FROM (
            SELECT 
                inv_visualizaciones.idlibro, inv_visualizaciones.fecha
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
        GROUP BY idlibro
        ORDER BY MAX(fecha) DESC, idlibro
        LIMIT 10 """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    resultados = [item[0] for item in resultados]
    return resultados


def INVObtenerLibrosRecomendados(idUsuario) :
    idsGenerosLibrosRecomendados = obtenerIdsGenerosLibrosRecomendados(idUsuario)

    idsGenerosLibrosRecomendados = ",".join(map(str, idsGenerosLibrosRecomendados))

    sql = """SELECT 
                MAX(cat_libros.id),
                MAX(cat_libros.titulo) ,
                MAX(cat_libros.precio),
                MAX(cat_libros.descuento),
                MAX(cat_libros.iva),
                MAX(cat_libros.idgenero) ,
                MAX(cat_libros.fechapublicacion),
                MAX(cat_libros.portada),
                MAX(cat_libros.sinopsis),
                MAX(cat_libros.paginas),

                MAX(conf_genero.genero),

                MAX(cat_idioma.id),

                MAX(cat_editoriales.editorial),

                STRING_AGG(CONCAT(conf_autores.nombre, ' ', conf_autores.apellidopaterno, ' ', conf_autores.apellidomaterno), '  ') AS autores,
                MAX(inv_inventariolibros.cantidad) AS limiteLibro
            FROM 
                cat_libros 
            LEFT JOIN 
                conf_genero ON cat_libros.idgenero = conf_genero.id
            LEFT JOIN 
                cat_idioma ON cat_libros.ididioma = cat_idioma.id
            LEFT JOIN 
                cat_editoriales ON cat_libros.ideditorial = cat_editoriales.id
            LEFT JOIN
                inv_inventariolibros ON cat_libros.id = inv_inventariolibros.idlibro
            LEFT JOIN 
                cat_librosautores ON cat_libros.id = cat_librosautores.idlibro
            JOIN 
                conf_autores ON cat_librosautores.idautor = conf_autores.idautor
            WHERE 
                cat_libros.idgenero IN (""" + idsGenerosLibrosRecomendados + """) AND
                cat_libros.activo = 'S'
            GROUP BY
                cat_libros.id
            ORDER BY 
                RANDOM()    
            LIMIT 10"""

    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def obtenerIdsGenerosLibrosRecomendados(idUsuario) :
    sql = """SELECT DISTINCT 
                cat_libros.idgenero, inv_visualizaciones.fecha
            FROM
                inv_visualizaciones
            JOIN
                cat_libros ON inv_visualizaciones.idlibro = cat_libros.id
            LEFT JOIN
                inv_inventariolibros ON inv_visualizaciones.idlibro = inv_inventariolibros.idlibro
            WHERE
                inv_visualizaciones.idusuario = '""" + str(idUsuario) + """' AND
                cat_libros.activo = 'S' AND
                inv_inventariolibros.cantidad > '0' AND
                inv_inventariolibros.cantidad IS NOT NULL
            ORDER BY inv_visualizaciones.fecha DESC
            LIMIT 5"""
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    if not resultados :
        sql = """SELECT DISTINCT 
                    cat_libros.idgenero, inv_visualizaciones.fecha
                FROM
                    inv_visualizaciones
                JOIN
                    cat_libros ON inv_visualizaciones.idlibro = cat_libros.id
                LEFT JOIN
                    inv_inventariolibros ON inv_visualizaciones.idlibro = inv_inventariolibros.idlibro
                WHERE
                    cat_libros.activo = 'S' AND
                    inv_inventariolibros.cantidad > '0' AND
                    inv_inventariolibros.cantidad IS NOT NULL
                ORDER BY inv_visualizaciones.fecha DESC
                LIMIT 5"""

        with connection.cursor() as cursor:
            cursor.execute(sql)
            resultados = cursor.fetchall()
    
    resultados = [item[0] for item in resultados]
    return resultados

def INVAgregarAumentarLibroCarrito(datosGenerales) :
    existenciaCarrito = comprobarExistenciaLibroCarrito(datosGenerales)
    
    if not existenciaCarrito :
        return agregarLibroCarrito(datosGenerales)
    else :
        cantidadLibroCarrito = existenciaCarrito[1]
        stockLibro = existenciaCarrito[2]
        if datosGenerales["cantidad"] + cantidadLibroCarrito > stockLibro :
            return False
        datosGenerales["idCarrito"] = existenciaCarrito[0]
        datosGenerales["cantidad"] += cantidadLibroCarrito
        return actualizarLibroCarritoCompra(datosGenerales)

def comprobarExistenciaLibroCarrito(datosGenerales) :
    sql = """SELECT
                ven_carrodecompra.id, ven_carrodecompra.cantidad,

                inv_inventariolibros.cantidad AS stock
            FROM
                ven_carrodecompra
            JOIN
                inv_inventariolibros ON ven_carrodecompra.idlibro = inv_inventariolibros.idlibro
            WHERE
                ven_carrodecompra.idusuario = '""" + str(datosGenerales["idUsuario"]) + """' AND
                ven_carrodecompra.idlibro = '""" + str(datosGenerales["idLibro"]) + """' """
    
    with connection.cursor() as cursor:
            cursor.execute(sql)
            resultado = cursor.fetchone()
    
    if not resultado :
        return False
    else :
        return resultado
    
def agregarLibroCarrito(datosGenerales) :
    idUsuario = datosGenerales["idUsuario"]
    idLibro = datosGenerales["idLibro"]
    cantidad = datosGenerales["cantidad"]

    try:
        with transaction.atomic():
            sql = """
                INSERT INTO ven_carrodecompra (idusuario, idlibro, cantidad, activo)
                VALUES ('"""+str(idUsuario)+"""', '"""+str(idLibro)+"""', '"""+str(cantidad)+"""', 'S')
            """
            
            with connection.cursor() as cursor:
                cursor.execute(sql)

        return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False 

def actualizarLibroCarritoCompra(datosGenerales) :
    sql = """UPDATE 
            ven_carrodecompra
        SET
            cantidad = '""" + str(datosGenerales["cantidad"]) + """'
        WHERE
            id = '""" + str(datosGenerales["idCarrito"]) + """'
        """
    
    try :
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(sql)
        return True
    except IntegrityError as e:
        print("Error en la Actualizacion, transacción revertida:", e)
        return False 
    
def INVObtenerLibrosCarritoCompra(idUsuario) :
    sql = """SELECT 
            ven_carrodecompra.idlibro,
            MAX(ven_carrodecompra.cantidad) AS cantidad,
            MAX(cat_libros.titulo) AS titulo,
            MAX(cat_libros.precio) AS precio,
            MAX(cat_libros.descuento) AS descuento,
            MAX(cat_libros.iva) AS iva,
            MAX(cat_libros.portada) AS portada,
            STRING_AGG(CONCAT(conf_autores.nombre, ' ', conf_autores.apellidopaterno, ' ', conf_autores.apellidomaterno), '  ') AS autor,
            MAX(inv_inventariolibros.cantidad) AS limiteLibro
        FROM
            ven_carrodecompra
        LEFT JOIN
            cat_libros ON ven_carrodecompra.idlibro = cat_libros.id
        LEFT JOIN
            inv_inventariolibros ON ven_carrodecompra.idlibro = inv_inventariolibros.idlibro
        LEFT JOIN
            cat_librosautores ON ven_carrodecompra.idlibro = cat_librosautores.idlibro
        LEFT JOIN
            conf_autores ON cat_librosautores.idautor = conf_autores.idautor
        WHERE
            ven_carrodecompra.idusuario = '""" + str(idUsuario) + """'
            AND ven_carrodecompra.activo = 'S' 
            AND cat_libros.activo = 'S'
            AND inv_inventariolibros.activo = 'S'
        GROUP BY
            ven_carrodecompra.idlibro"""
    
    try :
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(sql)
                resultado = cursor.fetchall()
        return resultado
    except IntegrityError as e:
        print("Error en la Actualizacion, transacción revertida:", e)
        return False 