from django.urls import path
from . import views
import digital.controller.login as login
import digital.controller.inventario as inventario
import digital.controller.configuracion as configuracion
import digital.controller.ventas as ventas
import digital.controller.administracion as administracion

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
    path("INVAgregarAumentarLibroCarrito/", inventario.INVAgregarAumentarLibroCarrito),
    path("INVObtenerLibrosCarritoCompra/", inventario.INVObtenerLibrosCarritoCompra),
    path("INVLimpiarCarritoCompra/", inventario.INVLimpiarCarritoCompra),
    path("INVBorrarLibroCarrito/", inventario.INVBorrarLibroCarrito),
    path("INVActualizarCantidadLibroCarrito/", inventario.INVActualizarCantidadLibroCarrito),
    path("INVRegistrarVisualizacion/", inventario.INVRegistrarVisualizacion),
    
    # CONFIGURACION
    path("CONFObtenerGenerosFiltros/", configuracion.CONFObtenerGenerosFiltros),
    path("CONFFiltrarLibros/", configuracion.CONFFiltrarLibros),

    # VENTAS
    path("VENRegistrarVenta/", ventas.VENRegistrarVenta),

    # ADMINISTRACION
    path("ADMObtenerLibros/", administracion.ADMObtenerLibros),

]