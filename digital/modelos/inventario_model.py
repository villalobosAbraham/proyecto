from django.db.models import Max, F
from django.db import transaction, IntegrityError
from digital.models import LogUsuarios, Visualizacion, CatLibros, InventarioLibro

def INVObtenerLibrosPopulares() :
    # Filtrar las visualizaciones con las condiciones dadas y unir tablas necesarias
    visualizaciones = (
        Visualizacion.objects
        .filter(
            catlibros__activo='S',                          # cat_libros.activo = 'S'
            invinventariolibros__cantidad__gt=0,            # inv_inventariolibros.cantidad > 0
            invinventariolibros__cantidad__isnull=False     # inv_inventariolibros.cantidad IS NOT NULL
        )
        .select_related('catlibros')                        # Equivale al JOIN de cat_libros
        .select_related('inv_inventariolibros')             # Equivale al LEFT JOIN de inv_inventariolibros
        .values('idlibro')                                  # Agrupar por idlibro
        .annotate(fecha_max=Max('fecha'))                   # Obtener MAX(fecha) por cada idlibro
        .order_by('-fecha_max')[:10]                        # Ordenar y limitar a los 10 más recientes
    )

    return visualizaciones