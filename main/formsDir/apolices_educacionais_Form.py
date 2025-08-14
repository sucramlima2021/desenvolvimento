from django import forms
from ..modelsDir.apolices_educacional import *
from .bases import BaseClienteForm

class ApolicesEForm(forms.ModelForm):
    class Meta:
        model = ApolicesE
        fields = '__all__'
        widgets = {
            'movimento': forms.RadioSelect(choices=ApolicesE.STATUS_CHOICES,attrs={'class': 'form-check-input'}),
            'datacancelamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'averbacao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'producao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'nascimento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        exclude = ('cliente',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        self.fields["apolice"].queryset = ApolicesGerais.objects.filter(tipo='educacional')