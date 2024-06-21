from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Moto
from django.urls import reverse_lazy
# Create your views here.

def Inicio(request):
    return render(request,'motos/inicio.html')



class Motos(ListView):
    model = Moto
    template_name = 'motos/lista_motos.html'
    context_object_name = 'motos'
    
class CrearMotos(CreateView):
    model = Moto
    template_name = 'motos/crear_moto.html'
    success_url = reverse_lazy('ListaMotos')
    fields = ['marca','modelo','año','kilometros']

class VerMoto(DetailView):
    model = Moto
    template_name = 'motos/ver_moto.html'


class EditarMoto(UpdateView):
    model = Moto
    template_name = 'motos/editar_moto.html'
    success_url = reverse_lazy('ListaMotos')
    fields = ['marca','modelo','año','kilometros']    
    
    
class EliminarMoto(DeleteView):
    model = Moto
    template_name = "motos/eliminar_moto.html"
    success_url = reverse_lazy('ListaMotos')
    

    
    


    