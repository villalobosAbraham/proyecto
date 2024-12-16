from django.db import transaction, IntegrityError, connection


def VENRegistrarVenta(datosGenerales) :
    comprobacion = comprobarCantidadLibrosCarritoInventario(datosGenerales["idUsuario"])
    librosCarrito = obtenerLibrosCarritoVenta(datosGenerales["idUsuario"])
    if not comprobacion or not librosCarrito :
        return False

    try:
        with transaction.atomic() :
            idVenta = registrarVentaMaestra(datosGenerales, librosCarrito)
            registrarVentasDetalle(idVenta, librosCarrito)
            registrarSalidaInventarioVenta(librosCarrito)
            limpiarCarroCompra(datosGenerales["idUsuario"])

        return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False 

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

def obtenerLibrosCarritoVenta(idUsuario) :
    sql = """SELECT 
                cat_libros.id,
                ven_carrodecompra.cantidad,
                cat_libros.precio,
                cat_libros.descuento,
                cat_libros.iva
            FROM
                ven_carrodecompra
            LEFT JOIN
                cat_libros ON ven_carrodecompra.idlibro = cat_libros.id
            LEFT JOIN
                inv_inventariolibros ON ven_carrodecompra.idlibro = inv_inventariolibros.idlibro
            WHERE
                ven_carrodecompra.idusuario = '""" + str(idUsuario) + """'
                AND ven_carrodecompra.activo = 'S'
                AND cat_libros.activo = 'S'
                AND inv_inventariolibros.activo = 'S'"""

    with connection.cursor() as cursor:
            cursor.execute(sql)
            resultados = cursor.fetchall()
    
    return resultados

def registrarVentaMaestra(datosGenerales, librosCarrito) :
    totalesMaestra = prepararTotalesVentaMaestra(librosCarrito)

    sql = """INSERT INTO
                ven_ventam
                (fecha, hora, idusuariocompra, idvendedor, importe, descuento, iva, total, idestadoentrega, idordenpaypal)
            VALUES
                ('""" + str(datosGenerales["fecha"]) + """', '""" + str(datosGenerales["hora"]) + """', '""" + str(datosGenerales["idUsuario"]) + """', '0', 
                '""" + str(totalesMaestra["importe"]) + """', '""" + str(totalesMaestra["descuento"]) + """', '""" + str(totalesMaestra["iva"]) + """', 
                '""" + str(totalesMaestra["total"]) + """', '1', '""" + str(datosGenerales["idOrdenPaypal"]) + """')
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
    
def prepararTotalesVentaMaestra(librosCarrito) :
    importe = 0
    descuento = 0
    iva = 0
    total = 0

    for libro in librosCarrito :
        importe += (libro[1] * libro[2])
        descuento += (libro[1] * libro[3])
        iva += (libro[1] * libro[4])

    total = importe - descuento + iva
    
    totales = {}
    totales["importe"] = round(importe, 2)
    totales["descuento"] = round(descuento, 2)
    totales["iva"] = round(iva, 2)
    totales["total"] = round(total, 2)
    
    return totales

def registrarVentasDetalle(idVenta, librosCarrito) :
    sql = """INSERT INTO 
                ven_ventad
                (idventa, idlibro, cantidad, precio, descuento, iva, total)
            VALUES
                (%s,%s,%s,%s,%s,%s,%s)"""
    
    inserciones = prepararInsercionesVentasDetalles(idVenta, librosCarrito)


    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.executemany(sql, inserciones)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False 
    
def prepararInsercionesVentasDetalles(idVenta, librosCarrito) :
    inserciones = []
    for libro in librosCarrito :
        total = (libro[2] - libro[3] + libro[4]) * libro[1]
        tupla = (
            idVenta,                      # ID de la venta
            libro[0],             # ID del libro
            libro[1],            # Cantidad de libros vendidos
            libro[2],              # Precio del libro
            libro[3],           # Descuento aplicado
            libro[4],                 # IVA aplicado
            total               # Total por este libro
        )

        inserciones.append(tupla)
    
    return inserciones

def registrarSalidaInventarioVenta(librosCarrito) :
    sql = """UPDATE
                inv_inventariolibros
            SET
                cantidad = cantidad - %s
            WHERE
                idlibro = %s"""
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                for libro in librosCarrito :
                    cursor.execute(sql, (libro[1], libro[0]))
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False 
    
def limpiarCarroCompra(idUsuario) :
    sql = """DELETE
        FROM
            ven_carrodecompra
        WHERE
            idusuario = '""" + str(idUsuario) + """'"""
    
    try:
        with transaction.atomic() :
            with connection.cursor() as cursor:
                cursor.execute(sql)
            return True
    except IntegrityError as e:
        print("Error en la inserción, transacción revertida:", e)
        return False 

def VENObtenerDetallesVenta(idVenta) :
    sql = """SELECT
                ven_ventad.idlibro, ven_ventad.cantidad, ven_ventad.precio, ven_ventad.descuento, ven_ventad.iva, ven_ventad.total,

                cat_libros.titulo, cat_libros.portada
            FROM
                ven_ventad
            JOIN 
                cat_libros ON ven_ventad.idlibro = cat_libros.id
            WHERE
                ven_ventad.idventa = '""" + str(idVenta) + """'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()
    
    return resultados

def VENObtenerVentasUsuario(idUsuario) :
    sql = """SELECT DISTINCT
                ven_ventam.id, ven_ventam.fecha, ven_ventam.total, ven_ventam.idusuariocompra, ven_ventam.idvendedor, ven_ventam.idestadoentrega, ven_ventam.idordenpaypal,

                log_usuarios.nombre, log_usuarios.apellidopaterno, log_usuarios.apellidomaterno,

                conf_estadoentrega.estado
            FROM
                ven_ventam
            LEFT JOIN
                log_usuarios ON ven_ventam.idvendedor = log_usuarios.id
            LEFT JOIN
                conf_estadoentrega ON ven_ventam.idestadoentrega = conf_estadoentrega.id
            WHERE
                ven_ventam.idusuariocompra = '""" + str(idUsuario) + """'"""
    
    with connection.cursor() as cursor:
        cursor.execute(sql)
        resultados = cursor.fetchall()
    
    return resultados