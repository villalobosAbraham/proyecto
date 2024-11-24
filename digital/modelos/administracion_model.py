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

def ADMAgregarLibroCatalogo(datosGenerales) :
    try:
        with transaction.atomic() :
        
            idLibro = insertarLibro(datosGenerales) 

            insertarLibroAutor(idLibro, datosGenerales["idAutor"])

            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False

def insertarLibro(datosGenerales) :
    sql = """INSERT INTO cat_libros
                (titulo, precio, descuento, iva, idgenero, fechapublicacion, portada, sinopsis, fecharegistro, paginas, ididioma, ideditorial, activo)
            VALUES
                ('""" + str(datosGenerales["titulo"]) + """', 
                '""" + str(datosGenerales["precio"]) + """', 
                '""" + str(datosGenerales["descuento"]) + """', 
                '""" + str(datosGenerales["iva"]) + """', 
                '""" + str(datosGenerales["idGenero"]) + """', 
                '""" + str(datosGenerales["fechaPublicacion"]) + """', 
                '""" + str(datosGenerales["portada"]) + """', 
                '""" + str(datosGenerales["sinopsis"]) + """', 
                '""" + str(datosGenerales["fecha"]) + """', 
                '""" + str(datosGenerales["paginasLibro"]) + """', 
                '""" + str(datosGenerales["idIdioma"]) + """', 
                '""" + str(datosGenerales["idEditorial"]) + """', 
                'S')
                RETURNING id"""
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
                id_generado = cursor.fetchone()[0]  # Recuperar el ID generado
            return id_generado
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def insertarLibroAutor(idLibro, idAutor) :
    sql = """INSERT INTO cat_librosautores
                (idlibro, idautor)
            VALUES
                ('""" + str(idLibro) + """', '""" + str(idAutor) + """')"""
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def ADMDeshabilitarLibro(idLibro) :
    sql = """UPDATE 
                cat_libros
            SET
                activo = 'N'
            WHERE
                id = '""" + str(idLibro) + """';
            UPDATE 
                inv_inventariolibros
            SET
                activo = 'N'
            WHERE
                idlibro = '""" + str(idLibro) + """';    
            UPDATE 
                ven_carrodecompra
            SET
                activo = 'N'
            WHERE
                idlibro = '""" + str(idLibro) + """';    
            """
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def ADMHabilitarLibro(idLibro) :
    sql = """UPDATE 
                cat_libros
            SET
                activo = 'S'
            WHERE
                id = '""" + str(idLibro) + """';
            UPDATE 
                inv_inventariolibros
            SET
                activo = 'S'
            WHERE
                idlibro = '""" + str(idLibro) + """';    
            UPDATE 
                ven_carrodecompra
            SET
                activo = 'S'
            WHERE
                idlibro = '""" + str(idLibro) + """';    
            """
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def ADMDeshabilitarAutor(idAutor) :
    idsLibros = obtenerIdsLibrosAutor(idAutor) 

    try:
        with transaction.atomic() :
            deshabilitarAutor(idAutor)
            for libro in idsLibros :
                ADMDeshabilitarLibro(libro)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False

def obtenerIdsLibrosAutor(idAutor) :
    sql = """SELECT
                idlibro
            FROM 
                cat_librosautores
            WHERE
                idautor = '""" + str(idAutor) + """'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    resultados = [item[0] for item in resultados]
    return resultados

def deshabilitarAutor(idAutor) :
    sql = """UPDATE 
                conf_autores
            SET
                activo = 'N'
            WHERE
                idautor = '""" + str(idAutor) + """'"""
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def ADMHabilitarAutor(idAutor) :
    sql = """UPDATE 
                conf_autores
            SET
                activo = 'S'
            WHERE
                idautor = '""" + str(idAutor) + """'"""

    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def ADMObtenerNacionesActivas() :
    sql = """SELECT
                id, nacionalidad, siglas
            FROM
                conf_nacionalidad
            WHERE
                activo = 'S'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados

def ADMAgregarAutor(datosGenerales) :
    sql = """INSERT INTO conf_autores
                (nombre, apellidopaterno, apellidomaterno, fechanacimiento, fecharegistro, idnacionalidad, activo)
            VALUES
                ('""" + str(datosGenerales["nombre"]) + """',
                '""" + str(datosGenerales["apellidoPaterno"]) + """',
                '""" + str(datosGenerales["apellidoMaterno"]) + """',
                '""" + str(datosGenerales["fechaNacimiento"]) + """',
                '""" + str(datosGenerales["fecha"]) + """',
                '""" + str(datosGenerales["idNacionalidad"]) + """',
                'S')"""
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False
    
def ADMObtenerInventarioLibros() :
    sql = """SELECT
                cat_libros.id, cat_libros.titulo, cat_libros.idgenero, cat_libros.ididioma, cat_libros.ideditorial,

                inv_inventariolibros.cantidad, inv_inventariolibros.activo,

                conf_genero.genero,

                cat_idioma.id,

                cat_editoriales.editorial
            FROM
                cat_libros
            LEFT JOIN
                inv_inventariolibros ON cat_libros.id = inv_inventariolibros.idlibro
            LEFT JOIN
                conf_genero ON cat_libros.idgenero = conf_genero.id
            LEFT JOIN
                cat_idioma ON cat_libros.ididioma = cat_idioma.id
            LEFT JOIN
                cat_editoriales ON cat_libros.ideditorial = cat_editoriales.id"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()

    return resultados