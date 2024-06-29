from django.urls import path 
from . import views

urlpatterns = [
    (path('mensajes/',views.contacto, name='Mensajes')),
    (path('mensajes/enviado',views.Mensaje_enviado, name='Mensaje_enviado')),
    (path('mensajes/lista',views.lista_mensajes, name='Lista_mensajes')),
    (path('mensajes/ver/<int:id>/',views.ver_mensaje, name='Ver_mensaje')),
    (path('mensajes/eliminar/<int:id>/',views.eliminar_mensaje, name='Eliminar_mensaje')),
    
]
