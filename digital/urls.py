from django.urls import path, re_path
from . import views
import digital.controller.login as login
import digital.controller.inventario as inventario
import digital.controller.configuracion as configuracion
import digital.controller.ventas as ventas
import digital.controller.administracion as administracion

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # LOGIN
    path("", login.index),
    path("LOGIniciarSesion/", login.LOGIniciarSesion),
    path("LOGRegistrarUsuario/", login.LOGRegistrarUsuario),
    path("LOGObtenerUsuarioBarra/", login.LOGObtenerUsuarioBarra),
    path("LOGGuardarInformacionUsuarioBarra/", login.LOGGuardarInformacionUsuarioBarra),
    path("LOGCerrarSesion/", login.LOGCerrarSesion),
    
    # INVENTARIO
    path("INVObtenerLibrosPopulares/", inventario.INVObtenerLibrosPopulares),
    path("INVObtenerLibrosRecomendados/", inventario.INVObtenerLibrosRecomendados),
    path("INVComprobarCarritoCantidad/", inventario.INVComprobarCarritoCantidad),
    path("INVAgregarAumentarLibroCarrito/", inventario.INVAgregarAumentarLibroCarrito),
    path("INVObtenerDetallesLibro/", inventario.INVObtenerDetallesLibro),
    path("INVObtenerLibrosCarritoCompra/", inventario.INVObtenerLibrosCarritoCompra),
    path("INVLimpiarCarritoCompra/", inventario.INVLimpiarCarritoCompra),
    path("INVBorrarLibroCarrito/", inventario.INVBorrarLibroCarrito),
    path("INVActualizarCantidadLibroCarrito/", inventario.INVActualizarCantidadLibroCarrito),
    path("INVRegistrarVisualizacion/", inventario.INVRegistrarVisualizacion),
    path("INVObtenerTotalesCarritoCompra/", inventario.INVObtenerTotalesCarritoCompra),
    
    # CONFIGURACION
    path("CONFObtenerGenerosFiltros/", configuracion.CONFObtenerGenerosFiltros),
    path("CONFFiltrarLibros/", configuracion.CONFFiltrarLibros),

    # VENTAS
    path("VENRegistrarVenta/", ventas.VENRegistrarVenta),
    path("VENObtenerDetallesVenta/", ventas.VENObtenerDetallesVenta),
    path("VENObtenerVentasUsuario/", ventas.VENObtenerVentasUsuario),

    # ADMINISTRACION
    path("ADMObtenerLibros/", administracion.ADMObtenerLibros),
    path("ADMObtenerAutoresActivos/", administracion.ADMObtenerAutoresActivos),
    path("ADMObtenerAutores/", administracion.ADMObtenerAutores),
    path("ADMObtenerEditoriales/", administracion.ADMObtenerEditoriales),    
    path("ADMAgregarEditorial/", administracion.ADMAgregarEditorial),    
    path("ADMHabilitarEditorial/", administracion.ADMHabilitarEditorial),    
    path("ADMDesHabilitarEditorial/", administracion.ADMDesHabilitarEditorial),    
    path("ADMObtenerGeneros/", administracion.ADMObtenerGeneros),
    path("ADMObtenerGenerosActivos/", administracion.ADMObtenerGenerosActivos),
    path("ADMDesHabilitarGenero/", administracion.ADMDesHabilitarGenero),
    path("ADMHabilitarGenero/", administracion.ADMHabilitarGenero),
    path("ADMObtenerEditorialesActivos/", administracion.ADMObtenerEditorialesActivos),
    path("ADMObtenerIdiomasActivos/", administracion.ADMObtenerIdiomasActivos),
    path("ADMAgregarLibroCatalogo/", administracion.ADMAgregarLibroCatalogo),
    path("ADMObenerLibroEdicion/", administracion.ADMObenerLibroEdicion),
    path("ADMDeshabilitarLibro/", administracion.ADMDeshabilitarLibro),
    path("ADMHabilitarLibro/", administracion.ADMHabilitarLibro),
    path("ADMEditarLibroCatalogo/", administracion.ADMEditarLibroCatalogo),
    path("ADMDeshabilitarAutor/", administracion.ADMDeshabilitarAutor),
    path("ADMHabilitarAutor/", administracion.ADMHabilitarAutor),
    path("ADMObtenerNacionesActivas/", administracion.ADMObtenerNacionesActivas),
    path("ADMAgregarAutor/", administracion.ADMAgregarAutor),
    path("ADMObtenerInventarioLibros/", administracion.ADMObtenerInventarioLibros),
    path("ADMModificarInventarioLibro/", administracion.ADMModificarInventarioLibro),
    path("ADMObtenerDatosInventarioLibro/", administracion.ADMObtenerDatosInventarioLibro),
    path("ADMHabilitarInventario/", administracion.ADMHabilitarInventario),
    path("ADMDeshabilitarInventario/", administracion.ADMDeshabilitarInventario),
    path("ADMObtenerVentas/", administracion.ADMObtenerVentas),
    path("ADMObtenerVenta/", administracion.ADMObtenerVenta),
    path("ADMEntregarVenta/", administracion.ADMEntregarVenta),
    path("ADMObtenerEmpleados/", administracion.ADMObtenerEmpleados),
    path("ADMRegistrarEmpleado/", administracion.ADMRegistrarEmpleado),
    path("ADMDeshabilitarEmpleado/", administracion.ADMDeshabilitarEmpleado),
    path("ADMHabilitarEmpleado/", administracion.ADMHabilitarEmpleado),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)