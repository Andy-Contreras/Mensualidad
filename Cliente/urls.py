from .views.clien.views import DetalleCliente,CrearCliente,EliminarCliente
from django.urls import path


app_name = "Cliente_gym"
urlpatterns = [
    # -- Cliente
    path('detalle_cliente/', DetalleCliente.as_view(), name="detalle_cliente"),
    path('crear_cliente/', CrearCliente.as_view(), name="crear_cliente"),
    path('eliminar_cliente/<int:pk>', EliminarCliente.as_view(), name="eliminar_cliente"),
]