from . import models
from django import forms

class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } # Estilização do formulário
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        } # Alterando o label para ficar em português
        
    def clean_quantity(self) -> int:
        """
        Validate that the requested quantity does not exceed the available quantity of the product.

        Raises:
            ValidationError: If the requested quantity is greater than the available product quantity.

        Returns:
            int: The validated quantity.
        """
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        if quantity > product.quantity:
            raise forms.ValidationError(f'A quantidade disponível em estoque para o produto "{product.title}" é de {product.quantity} unidades.')
        return quantity