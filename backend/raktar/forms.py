from django import forms
from .models import Alkatresz

class AlkatreszForm(forms.ModelForm):
    class Meta:
        model = Alkatresz
        fields = ['cikkszam', 'leiras', 'info', 'mertekegyseg', 'alkatreszcsoport', 'keszlet', 'listaar']
