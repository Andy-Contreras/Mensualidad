from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView
from Mensualidad.models import Mensualidad
from Mensualidad.forms import CabeceraMensual
from django.urls import reverse_lazy
from Trabajo.urls import *
# class MenuTemplateView(TemplateView):
#     template_name='Mensualidad.html'

#     def get_context_data(self,**kwargs ):
#         context = super().get_context_data(**kwargs)
#         context ['titulo'] = "Información"
#         return context


#Tabla
class DetalleMensualidad(ListView):
    template_name = 'Mensualidad.html'
    context_object_name = 'mensualidad'
    model = Mensualidad
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(id__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crear_url'] = '/Mensualidad_gym/crear_mensualidad/'
        context['url_anterior'] = "/"
        context['listar_url'] = '/Mensualidad_gym/menu/'
        context['titulo'] = 'Registro de Mensualidad'
        context['query'] = self.request.GET.get("query") or ""
        return context 

#Registro
class CrearMensualidad(CreateView):
    model = Mensualidad
    template_name = 'Crear.html'
    form_class = CabeceraMensual
    success_url = reverse_lazy('Mensualidad_gym:menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Mensualidad'
        context['action_save'] = self.request.path
        context['url_anterior'] = '/Mensualidad_gym/menu/'
        context['listar_url'] = '/Mensualidad_gym/menu/'

        return context

# Eliminar
class EliminarMensualidad(DeleteView):
    model = Mensualidad
    template_name = 'eliminar.html'
    success_url = reverse_lazy('Mensualidad_gym:menu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Eliminar Registro de Mensualidad'
        context['url_anterior'] = '/Mensualidad_gym/menu/'
        context['listar_url'] = '/Mensualidad_gym/menu/'
        return context

#Actualizar
class ActualizarMensualidad(UpdateView):
    model = Mensualidad
    template_name = 'editarmensu.html'
    success_url = reverse_lazy('Mensualidad_gym:menu')
    form_class = CabeceraMensual

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Actualizar Datos de la mensualidad'
        context['url_anterior'] = '/Mensualidad_gym/menu/'
        context['listar_url'] = '/Mensualidad_gym/menu/'
        return context


