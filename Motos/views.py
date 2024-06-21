from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Moto
# Create your views here.

class Motos(ListView):
    model = Moto
    template_name = 'motos/lista_motos.html'
    context_object_name = 'motos'
    