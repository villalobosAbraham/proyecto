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

def CONFFiltrarLibros(datosGenerales) :
    generos = datosGenerales["generos"]
    libro = datosGenerales["libro"].lower()
    sql = """SELECT 
                cat_libros.id,
                cat_libros.titulo,
                cat_libros.precio,
                cat_libros.descuento,
                cat_libros.iva,
                cat_libros.fechapublicacion,
                cat_libros.portada,
                cat_libros.sinopsis,
                cat_libros.paginas,
                conf_genero.genero,
                cat_editoriales.editorial,
                STRING_AGG(CONCAT(conf_autores.nombre, ' ', conf_autores.apellidopaterno, ' ', conf_autores.apellidomaterno), ' y ') AS autores,
                inv_inventariolibros.cantidad AS limiteLibro
            FROM 
                cat_libros 
            JOIN 
                conf_genero ON cat_libros.idgenero = conf_genero.id
            JOIN 
                cat_idioma ON cat_libros.ididioma = cat_idioma.id
            JOIN 
                cat_editoriales ON cat_libros.ideditorial = cat_editoriales.id
            JOIN
                inv_inventariolibros ON cat_libros.id = inv_inventariolibros.idlibro
            JOIN 
                cat_librosautores ON cat_libros.id = cat_librosautores.idlibro
            JOIN 
                conf_autores ON cat_librosautores.idautor = conf_autores.idautor
            WHERE 
                cat_libros.activo = 'S' AND
                inv_inventariolibros.cantidad > '0' AND
                inv_inventariolibros.cantidad is not null AND
                inv_inventariolibros.activo = 'S' """
    
    if generos and libro :
        sql += """AND cat_libros.idgenero IN (""" + generos + """)
            OR LOWER(cat_libros.titulo) LIKE LOWER('%""" + str(libro) + """%') 
            OR LOWER(conf_autores.nombre) LIKE LOWER('%""" + str(libro) + """%') 
            OR LOWER(conf_autores.apellidopaterno) LIKE LOWER('%""" + str(libro) + """%') 
            OR LOWER(conf_autores.apellidomaterno) LIKE LOWER('%""" + str(libro) + """%')"""
    elif not libro :
        sql += """" AND cat_libros.idgeneroprincipal IN (""" + generos + """)"""
    elif not generos :
        sql += """AND LOWER(cat_libros.titulo) LIKE LOWER('%""" + str(libro) + """%') 
            OR LOWER(conf_autores.nombre) LIKE LOWER('%""" + str(libro) + """%') 
            OR LOWER(conf_autores.apellidopaterno) LIKE LOWER('%""" + str(libro) + """%') 
            OR LOWER(conf_autores.apellidomaterno) LIKE LOWER('%""" + str(libro) + """%')"""
        
    sql += """GROUP BY
            cat_libros.id, genero, editorial, cantidad"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados