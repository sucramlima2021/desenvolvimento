from django import forms
from ..modelsDir.clientes import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'nascimento': forms.DateInput(attrs={'type': 'date'}),
            'expedicao': forms.DateInput(attrs={'type': 'date'}),
            'nascimentoconjuge': forms.DateInput(attrs={'type': 'date'}),
            'dataanuencia': forms.DateInput(attrs={'type': 'date'}),
            'master': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'