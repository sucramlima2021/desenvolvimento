from django import forms
from ..modelsDir.apolices_sem_ifptd import *
from .bases import BaseClienteForm

class ApolicesSIFPTDForm(BaseClienteForm):
    class Meta:
        model = ApolicesSIFPTD
        fields = '__all__'

class HistoricoSIFPTDForm(forms.ModelForm):
    class Meta:
        model = HistoricoSIFPTD
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'