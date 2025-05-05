from django import forms
from ..modelsDir.apolices_mulher import *
from .bases import BaseClienteForm

class ApolicesMForm(BaseClienteForm):
    class Meta:
        model = ApolicesM
        fields = '__all__'

class HistoricoMForm(forms.ModelForm):
    class Meta:
        model = HistoricoM
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'