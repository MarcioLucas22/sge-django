from . import models
from django import forms

class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } # Estilização do formulário
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
        } # Alterando o label para ficar em português