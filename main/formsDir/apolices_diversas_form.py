from django import forms
from ..modelsDir.apolices_diversas import *


class ApolicesVidaForm(forms.ModelForm):
    class Meta:
        model = ApolicesVida
        fields = '__all__'
    
        widgets = {
            'movimento': forms.RadioSelect(choices=ApolicesVida.STATUS_CHOICES,attrs={'class': 'form-check-input'}),
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'datacancelamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'emissao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'referencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            
        }
        exclude = ('cliente',)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        
        
        self.fields["apolice"].queryset = ApolicesGerais.objects.filter(tipo='vida')


class ApolicesResidenciaForm(forms.ModelForm):
    class Meta:
        model = ApolicesResidencia
        fields = '__all__'
    
        widgets = {
            'movimento': forms.RadioSelect(choices=ApolicesVida.STATUS_CHOICES,attrs={'class': 'form-check-input'}),
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'datacancelamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'emissao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'versao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            
        }
        exclude = ('cliente',)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        
        
        self.fields["apolice"].queryset = ApolicesGerais.objects.filter(tipo='residencia')

class ApolicesMotoForm(forms.ModelForm):
    class Meta:
        model = ApolicesMoto
        fields = '__all__'
    
        widgets = {
            'movimento': forms.RadioSelect(choices=ApolicesVida.STATUS_CHOICES,attrs={'class': 'form-check-input'}),
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'datacancelamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'emissao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'versao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),  
        }
        exclude = ('cliente',)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        
        
        self.fields["apolice"].queryset = ApolicesGerais.objects.filter(tipo='moto')


class ApolicesCarroForm(forms.ModelForm):
    class Meta:
        model = ApolicesCarro
        fields = '__all__'
    
        widgets = {
            'movimento': forms.RadioSelect(choices=ApolicesVida.STATUS_CHOICES,attrs={'class': 'form-check-input'}),
            'inicio': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'datacancelamento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'emissao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'versao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),  
        }
        exclude = ('cliente',)

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class', '')
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = f'{existing_classes} form-control form-control-sm'
        
        
        self.fields["apolice"].queryset = ApolicesGerais.objects.filter(tipo='carro')