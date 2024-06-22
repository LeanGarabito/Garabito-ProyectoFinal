from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm 
from django.contrib.auth import authenticate, login
from User.forms import FormularioCrearuser,EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# Create your views here.

def log(request):
    formulario = AuthenticationForm()
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
            user = authenticate(request, username=usuario,password=contra)
            login(request,user)
            return redirect('Inicio')
    
    return render(request,'usuarios/login.html',{'formulario': formulario})

def register(request):
    formulario = FormularioCrearuser()
    if request.method == "POST":
        formulario = FormularioCrearuser(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Login')
    return render(request,'usuarios/register.html',{'formulario':formulario})

@login_required
def editar_perfil(request):
    formulario= EditarPerfil(instance=request.user)
    if request.method == "POST":
        formulario = EditarPerfil(request.POST,instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('EditarPerfil')
    return render(request,'usuarios/editar_perfil.html',{'formulario':formulario})



class cambiar_password(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contra.html'
    sussecess_url = reverse_lazy('EditarPerfil')
    
    

    

