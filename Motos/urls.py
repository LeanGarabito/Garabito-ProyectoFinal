from django.urls import path
from . import views


urlpatterns = [
    path('Motos/',views.Motos.as_view(), name='ListaMotos')   
]
