from .views.menu.views import *
from django.urls import path

app_name = "Mensualidad_gym"
urlpatterns = [
    # -- Mensualidad
    
    path('menu/', DetalleMensualidad.as_view(), name="menu"),
    path('crear_mensualidad/', CrearMensualidad.as_view(), name="crear_mensualidad"),
    path('eliminar_mensualidad/<int:pk>', EliminarMensualidad.as_view(), name="eliminar_mensualidad"),
    path('actualizar_mensualidad/<int:pk>', ActualizarMensualidad.as_view(), name="actualizar_mensualidad"),


]