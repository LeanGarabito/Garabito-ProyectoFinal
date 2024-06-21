from django.urls import path
from . import views


urlpatterns = [
    path('',views.Inicio, name='Inicio'),
    path('Motos/',views.Motos.as_view(), name='ListaMotos'),
    path('Motos/crear',views.CrearMotos.as_view(), name='CrearMoto'),
    path('Motos/<int:pk>',views.VerMoto.as_view(), name='VerMoto'),  
    path('Motos/<int:pk>/editar',views.EditarMoto.as_view(), name='EditarMoto'),
    path('Motos/<int:pk>/eliminar',views.EliminarMoto.as_view(), name='EliminarMoto')                 
                     
                   
]
