from django import forms
from ..modelsDir.agregados import *
from .bases import BaseClienteForm

class AgregadosForm(BaseClienteForm):
    class Meta:
        model = Agregados
        fields = '__all__'

