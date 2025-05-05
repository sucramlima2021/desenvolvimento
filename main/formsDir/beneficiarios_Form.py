from django import forms
from ..modelsDir.beneficiarios import *
from .bases import BaseClienteForm

class BeneficiariosForm(BaseClienteForm):
    class Meta:
        model = Beneficiarios
        fields = '__all__'

