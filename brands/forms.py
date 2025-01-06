from . import models
from django import forms

class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } # Estilização do formulário
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        } # Alterando o label para ficar em português