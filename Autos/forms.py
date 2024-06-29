from django import forms

class BuscarAuto(forms.Form):
    marca = forms.CharField(max_length=20, required=False)