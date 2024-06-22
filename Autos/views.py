from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Auto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaAuto(ListView):
    model = Auto
    template_name = 'Autos/lista_autos.html'
    context_object_name = 'Autos'
    
class CrearAuto(LoginRequiredMixin, CreateView):
    model = Auto
    template_name = 'Autos/crear_auto.html'
    success_url = reverse_lazy('ListaAutos')
    fields = ['marca','modelo','año','kilometros']

class VerAuto(DetailView):
    model = Auto
    template_name = 'Autos/ver_auto.html'


class EditarAuto(LoginRequiredMixin, UpdateView):
    model = Auto
    template_name = 'Autos/editar_auto.html'
    success_url = reverse_lazy('ListaAutos')
    fields = ['marca','modelo','año','kilometros']    
    
    
class EliminarAuto(LoginRequiredMixin,DeleteView):
    model = Auto
    template_name = "Autos/eliminar_auto.html"
    success_url = reverse_lazy('ListaAutos')
    
