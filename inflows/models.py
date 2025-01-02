from django.db import models
from suppliers.models import Supplier
from products.models import Products

class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # o hífen na frente é pra colocar como decrescente. Por padrão é crescente

    def __str__(self):
        return str(self.product) # transforma pra string pois valor nulo n é aceito