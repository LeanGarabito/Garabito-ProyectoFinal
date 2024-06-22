from django.urls import path
from . import views
urlpatterns = [
    path('Autos/',views.ListaAuto.as_view(), name='ListaAutos'),
    path('Autos/crear',views.CrearAuto.as_view(), name='CrearAuto'),
    path('Autos/<int:pk>',views.VerAuto.as_view(), name='VerAuto'),  
    path('Autos/<int:pk>/editar',views.EditarAuto.as_view(), name='EditarAuto'),
    path('Autos/<int:pk>/eliminar',views.EliminarAuto.as_view(), name='EliminarAuto') 
]
