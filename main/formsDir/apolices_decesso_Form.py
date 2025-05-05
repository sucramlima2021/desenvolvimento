from django import forms
from ..modelsDir.apolices_decesso import *
from .bases import BaseClienteForm

class DecessoForm(BaseClienteForm):
    class Meta:
        model = Decesso
        fields = '__all__'

class HistoricoDecessoForm(forms.ModelForm):
    class Meta:
        model = HistoricoDecesso
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'