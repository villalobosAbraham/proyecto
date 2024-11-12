from django.urls import path
from . import views
import digital.controller.login as login
import digital.controller.inventario as inventario

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
    
]