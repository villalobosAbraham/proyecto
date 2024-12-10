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
                conf_genero.activo = 'S' AND
                cat_libros.activo = 'S'
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
                
                STRING_AGG(CONCAT(conf_autores.nombre, ' ', conf_autores.apellidopaterno, ' ', conf_autores.apellidomaterno), ' y ') AS autores,
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
    elif generos :
        sql += """ AND cat_libros.idgenero IN (""" + generos + """)"""
    elif libro :
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
