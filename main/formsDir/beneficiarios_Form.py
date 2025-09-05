from django import forms
from ..modelsDir.beneficiarios import *

from ..modelsDir.angariadores import *

class BeneficiariosForm(forms.ModelForm):
    class Meta:
        model = BeneficiariosNovos
        fields = '__all__'
        widgets = {
           'nascimento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            
        }
        exclude = ('cliente', 'controle')
    
    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        if cliente:
            self.fields['apolice'].queryset = ApoliceBase.objects.filter(cliente=cliente)