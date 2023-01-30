from django.views.generic import TemplateView,ListView,CreateView, DeleteView
from Cliente.models import *
from Cliente.forms import *
from django.urls import reverse_lazy

# class PrincipalTemplateView(TemplateView):
#     template_name='detalle.html'

#     def get_context_data(self,**kwargs ):
#         context = super().get_context_data(**kwargs)
#         context ['titulo'] = "Clientes Registrados"
#         context ['url_anterior'] = "/"
#         return context

# Tabla
class DetalleCliente(ListView):
    template_name = 'detalle.html'
    context_object_name = 'cliente'
    model = Clientes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/'
        context['listar_url'] = '/Cliente_gym/detalle_cliente/'
        context['titulo'] = 'Registro de Cliente'
        return context 

#Registros 
class CrearCliente(CreateView):
    model = Clientes
    template_name = 'crearcliente.html'
    form_class = ClienteForms
    success_url = reverse_lazy('Cliente_gym:detalle_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registro de clientes'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/Cliente_gym/detalle_cliente/'
        context['listar_url'] = '/Cliente_gym/detalle_cliente/'

        return context

# Eliminar
class EliminarCliente(DeleteView):
    model = Clientes
    template_name = 'eliminarcliente.html'
    success_url = reverse_lazy('Cliente_gym:detalle_cliente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registro de Clientes'
        context['url_anterior'] = '/Cliente_gym/detalle_cliente/'
        context['listar_url'] = '/Cliente_gym/detalle_cliente/'
        return context
    