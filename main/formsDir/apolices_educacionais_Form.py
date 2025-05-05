from django import forms
from ..modelsDir.apolices_educacional import *
from .bases import BaseClienteForm

class ApolicesEForm(BaseClienteForm):
    class Meta:
        model = ApolicesE
        fields = '__all__'

class HistoricoEForm(forms.ModelForm):
    class Meta:
        model = HistoricoE
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'