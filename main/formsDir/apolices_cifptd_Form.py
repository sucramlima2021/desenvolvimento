from django import forms
from ..modelsDir.apolices_com_ifptd import *
from .bases import BaseClienteForm

class ApolicesCIFPTDForm(BaseClienteForm):
    class Meta:
        model = ApolicesCIFPTD
        fields = '__all__'

class HistoricoCIFPTDForm(forms.ModelForm):
    class Meta:
        model = HistoricoCIFPTD
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'