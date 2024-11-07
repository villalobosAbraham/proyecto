from django.db import models

# Create your models here.
class CatIdioma(models.Model):
    id = models.AutoField(primary_key=True)  # AUTO_INCREMENT equivalente
    idioma = models.CharField(max_length=255)  # VARCHAR(255)
    activo = models.CharField(max_length=1)  # CHAR(1)

    class Meta:
        db_table = 'cat_idioma'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Idiomas'
        ordering = ['id']  # Puedes especificar el ordenamiento si es necesario

    def __str__(self):
        return self.idioma
    
class CatEditoriales(models.Model):
    id = models.AutoField(primary_key=True) 
    editorial = models.CharField(max_length=255) 
    activo = models.CharField(max_length=1)  

    class Meta:
        db_table = 'cat_editoriales' 
        verbose_name_plural = 'Editoriales'
        ordering = ['id']  

    def __str__(self):
        return self.editorial
    
class ConfEstadoEntrega(models.Model):
    id = models.AutoField(primary_key=True)  
    estado = models.CharField(max_length=255) 
    activo = models.CharField(max_length=1)  

    class Meta:
        db_table = 'conf_estadoentrega' 
        verbose_name_plural = 'Estados de Entrega'  
        ordering = ['id']  

    def __str__(self):
        return self.estado  
    
class ConfGenero(models.Model):
    id = models.AutoField(primary_key=True)  
    genero = models.CharField(max_length=255)  
    activo = models.CharField(max_length=1)  

    class Meta:
        db_table = 'conf_genero'  
        verbose_name_plural = 'Géneros'  
        ordering = ['id']  

    def __str__(self):
        return self.genero 
    
class ConfNacionalidad(models.Model):
    id = models.AutoField(primary_key=True)  
    nacionalidad = models.CharField(max_length=255)  
    siglas = models.CharField(max_length=5)  
    activo = models.CharField(max_length=1)  

    class Meta:
        db_table = 'conf_nacionalidad'  
        verbose_name_plural = 'Nacionalidades'  
        ordering = ['id']  

    def __str__(self):
        return self.nacionalidad  
    
class LogTipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)  
    tipo = models.CharField(max_length=255)  
    activo = models.CharField(max_length=1)  

    class Meta:
        db_table = 'log_tipousuario'  
        verbose_name_plural = 'Tipos de Usuario'  
        ordering = ['id']  

    def __str__(self):
        return self.tipo  

class LogUsuarios(models.Model):
    id = models.AutoField(primary_key=True)  
    email = models.EmailField(max_length=255)   
    contraseña = models.CharField(max_length=255)   
    nombre = models.CharField(max_length=255)   
    apellidopaterno = models.CharField(max_length=255)   
    apellidomaterno = models.CharField(max_length=255)   
    idtipousuario = models.ForeignKey(
        'LogTipoUsuario', 
        on_delete=models.RESTRICT,  # FOREIGN KEY hacia LogTipoUsuario, ON DELETE RESTRICT
        db_column='idtipousuario'  # Nombre del campo en la base de datos
    )
    fecharegistro = models.DateField()  # DATE para la fecha de registro
    telefono = models.CharField(max_length=15, null=True, blank=True, default=None) 
    fechanacimiento = models.DateField(null=True, blank=True, default=None)
    activo = models.CharField(max_length=1)   

    class Meta:
        db_table = 'log_usuarios'  
        verbose_name_plural = 'Usuarios'  
        ordering = ['id']  # Orden por idusuario

    def __str__(self):
        return self.email  # Muestra el valor del campo 'email'
        
class ConfAutor(models.Model):
    idautor = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    nombre = models.CharField(max_length=255)     # Nombre del autor
    apellidopaterno = models.CharField(max_length=255)  # Apellido paterno
    apellidomaterno = models.CharField(max_length=255)   # Apellido materno
    fechanacimiento = models.DateField()           # Fecha de nacimiento
    fecharegistro = models.DateField ()              # Fecha de registro
    idnacionalidad =  models.ForeignKey(
        'ConfNacionalidad', 
        on_delete=models.RESTRICT,  # FOREIGN KEY hacia CatIdioma, ON DELETE RESTRICT
        db_column='idnacionalidad'
    )        # ID de nacionalidad (usando IntegerField para simplificar)
    activo = models.CharField(max_length=1, null=True, default=None)  # Estado activo del autor

    class Meta:
        db_table = 'conf_autores'                     # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Autores'                # Nombre plural del modelo
        indexes = [
            models.Index(fields=['idnacionalidad']),  # Índice para el campo idnacionalidad
        ]

    def __str__(self):
        return f"{self.nombre} {self.apellidopaterno} {self.apellidomaterno}"  # Representación en cadena del autor

class CatLibros(models.Model):
    id = models.AutoField(primary_key=True)  # AUTO_INCREMENT y PRIMARY KEY
    titulo = models.CharField(max_length=255)  # VARCHAR(255)
    precio = models.FloatField()  # FLOAT(32, 0) para precio
    descuento = models.FloatField()  # FLOAT(32, 0) para descuento
    iva = models.FloatField()  # FLOAT(32, 0) para IVA
    fechapublicacion = models.DateField()  # DATE para la fecha de publicación
    portada = models.CharField(max_length=100, null=True, blank=True, default=None)  # VARCHAR(100), puede ser NULL
    sinopsis = models.CharField(max_length=1000)  # VARCHAR(1000) para la sinopsis
    fecharegistro = models.DateField()  # DATE para la fecha de registro
    paginas = models.IntegerField()  # INT para el número de páginas
    activo = models.CharField(max_length=1)
    ideditorial = models.ForeignKey(
        'CatEditoriales', 
        on_delete=models.RESTRICT,  # FOREIGN KEY hacia CatEditoriales, ON DELETE RESTRICT
        db_column='ideditorial'
    )
    ididioma = models.ForeignKey(
        'CatIdioma', 
        on_delete=models.RESTRICT,  # FOREIGN KEY hacia CatIdioma, ON DELETE RESTRICT
        db_column='ididioma'
    )
    idgenero = models.ForeignKey(
        'ConfGenero', 
        on_delete=models.RESTRICT,  # FOREIGN KEY hacia ConfGenero, ON DELETE RESTRICT
        db_column='idgenero'
    )  

    class Meta:
        db_table = 'cat_libros'  
        verbose_name_plural = 'Libros'  
        ordering = ['id']  

    def __str__(self):
        return self.titulo  # Muestra el valor del campo 'titulo'
    
class LibroAutor(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    idlibro = models.ForeignKey(
        "CatLibros",  # Referencia al modelo Libro
        on_delete=models.RESTRICT,
        db_column='idlibro'
    )
    idautor = models.ForeignKey(
        "ConfAutor",  # Referencia al modelo Autor
        on_delete=models.RESTRICT,
        db_column='idautor'
    )

    class Meta:
        db_table = 'cat_librosautores'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Relacion Libros Autores'
        ordering = ['id']  


    def __str__(self):
        return f"Detalle ID: {self.id}, Libro: {self.idlibro}, Autor: {self.idautor}"
    
class InventarioLibro(models.Model):
    id = models.AutoField(primary_key=True)       # Clave primaria auto incremental
    idlibro = models.ForeignKey(
        'CatLibros',  
        on_delete=models.RESTRICT,  # Comportamiento al eliminar
        db_column='idlibro'  # Nombre de la columna en la tabla
    )
    cantidad = models.IntegerField()               # Cantidad de libros en inventario
    activo = models.CharField(max_length=1)       # Estado activo del inventario

    class Meta:
        db_table = 'inv_inventariolibros'           # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Inventarios de Libros'
        ordering = ['id'] 

    def __str__(self):
        return f"Inventario ID: {self.id}, Cantidad: {self.cantidad}, Activo: {self.activo}"
    
class CarroDeCompra(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    idusuario = models.ForeignKey(
        "LogUsuarios",
        on_delete=models.RESTRICT,  
        db_column='idusuario'  
    )  
    idlibro = models.ForeignKey(
        "CatLibros",
        on_delete=models.RESTRICT,  
        db_column='idlibro'  
    )
    cantidad = models.IntegerField()
    activo = models.CharField(max_length=1)

    class Meta:
        db_table = 'ven_carrodecompra'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Carro de compra'
        ordering = ['id'] 

    def __str__(self):
        return f"Carro ID: {self.id}, Usuario: {self.idusuario}, Libro: {self.idlibro}"

class Visualizacion(models.Model):
    id = models.BigAutoField(primary_key=True)  # Clave primaria auto incremental
    idusuario = models.ForeignKey(
        "LogUsuarios",
        on_delete=models.RESTRICT,  
        db_column='idusuario'  
    )   
    idlibro = models.ForeignKey(
        "CatLibros",
        on_delete=models.RESTRICT,  
        db_column='idlibro'  
    )
    fecha = models.DateField()

    class Meta:
        db_table = 'inv_visualizaciones'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Visualizaciones'
        ordering = ['id'] 

    def __str__(self):
        return f"Visualización ID: {self.idvisualizacion}, Usuario: {self.idusuario}, Libro: {self.idlibro}, Fecha: {self.fecha}"
    
class Venta(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    fecha = models.DateField()
    hora = models.TimeField()
    idusuariocompra = models.ForeignKey(
        "LogUsuarios",
        on_delete=models.RESTRICT,  
        db_column='idusuariocompra',
        related_name='ventas_comprador'  
    )
    idvendedor = models.ForeignKey(
        "LogUsuarios",
        on_delete=models.RESTRICT,  
        db_column='idvendedor',
        related_name='ventas_vendedor'  
    )
    importe = models.FloatField()
    descuento = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    idestadoentrega = models.ForeignKey(
        'ConfEstadoEntrega',  
        on_delete=models.CASCADE,
        db_column='idestadoentrega'
    )
    idordenpaypal = models.CharField(max_length=255)

    class Meta:
        db_table = 'ven_ventam'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Ventas Masetra'
        ordering = ['id', 'fecha', 'hora', 'idusuariocompra', 'idvendedor', 'importe', 'descuento', 'iva', 'total', 'idestadoentrega', 'idordenpaypal']

    def __str__(self):
        return f"Venta ID: {self.id}, Fecha: {self.fecha}, Importe: {self.importe}"
    
class VentaDetalle(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria auto incremental
    idventa = models.ForeignKey(
        'Venta',  
        on_delete=models.RESTRICT,
        db_column='idventa'
    )
    idlibro = models.ForeignKey(
        'CatLibros',  # Referencia al modelo Libro
        on_delete=models.RESTRICT,
        db_column='idlibro'
    )
    cantidad = models.IntegerField()
    precio = models.FloatField()
    descuento = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()

    class Meta:
        db_table = 'ven_ventad'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Ventas Detalles'
        ordering = ['id'] 

    def __str__(self):
        return f"Detalle ID: {self.id}, Venta ID: {self.idventa}, Libro ID: {self.idlibro}"