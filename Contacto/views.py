from django.shortcuts import render,redirect
from .forms import ContactoFormulario
from .models import Contacto
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.
def contacto(request):
    formulario = ContactoFormulario()
    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            mensaje = Contacto(nombre=datos.get('nombre'),
                               email=datos.get('email'),
                               asunto=datos.get('asunto'),
                               mensaje=datos.get('mensaje'))
            formulario.save()
            return redirect('Mensaje_enviado')
    
    return render(request,'Contacto/mensajes.html',{'formulario':formulario})

def Mensaje_enviado(request):
    return render(request,'Contacto/mensaje_enviado.html')
@login_required
def lista_mensajes(request):
    mensajes = Contacto.objects.all()
    return render(request,'Contacto/lista_mensajes.html', {'mensajes': mensajes})

@login_required
def ver_mensaje(request,id):
    mensaje = Contacto.objects.get(id=id)       
    return render(request,'Contacto/ver_mensaje.html', {'mensaje':mensaje})
@login_required
def eliminar_mensaje(request,id):
    mensaje = Contacto.objects.get(id=id)
    mensaje.delete()
    return redirect('Lista_mensajes')
    
