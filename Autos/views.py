from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Auto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BuscarAuto

# class ListaAuto(ListView):
#     model = Auto
#     template_name = 'Autos/lista_autos.html'
#     context_object_name = 'Autos'
    
def autos(request):
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data['marca']
        autos = Auto.objects.filter(marca__icontains=marca)
    return render(request, 'Autos/lista_autos.html', {'autos': autos, 'formulario': formulario})
    
class CrearAuto(LoginRequiredMixin, CreateView):
    model = Auto
    template_name = 'Autos/crear_auto.html'
    success_url = reverse_lazy('ListaAutos')
    fields = ['marca','modelo','año','kilometros','imagen']

class VerAuto(DetailView):
    model = Auto
    template_name = 'Autos/ver_auto.html'


class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = 'Autos/editar_auto.html'
    success_url = reverse_lazy('ListaAutos')
    fields = ['marca','modelo','año','kilometros','imagen']    
    
    
class EliminarAuto(LoginRequiredMixin,DeleteView):
    model = Auto
    template_name = "Autos/eliminar_auto.html"
    success_url = reverse_lazy('ListaAutos')
    
