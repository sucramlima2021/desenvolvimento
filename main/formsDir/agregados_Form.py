from django import forms
from ..modelsDir.agregados import *

from ..modelsDir.angariadores import *

class AgregadosForm(forms.ModelForm):
    class Meta:
        model = Agregados
        fields = '__all__'
        widgets = {
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'nascimento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            
        }
        exclude = ('cliente', 'subconv', 'nivel')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'