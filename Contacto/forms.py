
from django import forms
from .models import Contacto

class ContactoFormulario(forms.ModelForm): 
    class Meta:
        model = Contacto
        fields = ['nombre','email','asunto','mensaje']