from django.db.models import Max, F
from django.db import transaction, IntegrityError, connection

def ADMObtenerLibros() :
    sql = """SELECT 
                cat_libros.id AS idlibro,
                cat_libros.titulo,
                cat_libros.precio,
                cat_libros.descuento,
                cat_libros.iva,
                cat_libros.idgenero,
                cat_libros.fechapublicacion,
                cat_libros.portada,
                cat_libros.sinopsis,
                cat_libros.paginas,
                cat_libros.activo,

                conf_genero.genero,

                cat_idioma.id AS idioma,

                cat_editoriales.editorial,

                STRING_AGG(CONCAT(conf_autores.nombre, ' ', conf_autores.apellidopaterno, ' ', conf_autores.apellidomaterno), '  ') AS autores,
                
                inv_inventariolibros.cantidad
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
            GROUP BY
                cat_libros.id, conf_genero.genero, cat_idioma.id, cat_editoriales.editorial, inv_inventariolibros.cantidad"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def ADMObtenerAutoresActivos() :
    sql = """SELECT
                idautor, nombre, apellidopaterno, apellidomaterno
            FROM
                conf_autores
            WHERE
                activo = 'S'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def ADMObtenerAutores() :
    sql = """SELECT
                conf_autores.idautor, conf_autores.nombre, conf_autores.apellidopaterno, 
                conf_autores.apellidomaterno, conf_autores.fechanacimiento, conf_autores.idnacionalidad,
                conf_autores.activo,

                conf_nacionalidad.nacionalidad
            FROM
                conf_autores
            JOIN 
                conf_nacionalidad ON conf_autores.idnacionalidad = conf_nacionalidad.id"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def ADMObtenerGenerosActivos() :
    sql = """SELECT
                id, genero
            FROM
                conf_genero
            WHERE
                activo = 'S'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def ADMObtenerEditorialesActivos() :
    sql = """SELECT
                id, editorial
            FROM
                cat_editoriales
            WHERE
                activo = 'S'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def ADMObtenerIdiomasActivos() :
    sql = """SELECT
                id, idioma
            FROM
                cat_idioma
            WHERE
                activo = 'S'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados