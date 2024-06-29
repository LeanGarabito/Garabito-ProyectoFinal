from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('Login/',views.log, name=("Login")),
    path('Logout/', LogoutView.as_view(template_name='usuarios/logout.html') , name=("Logout")),
    path('Registro/',views.register, name=("Register")),
    path('About/',views.about, name=("About")),
    path('VerPerfil/',views.Usuario, name=("VerPerfil")),
    path('EditarPerfil/', views.editar_perfil, name=('EditarPerfil')),
    path('EditarPerfil/Password',views.cambiar_password.as_view(), name=('EditarContra'))
    
]
