from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from categories.models import Category
from brands.models import Brand
import app.metrics as metrics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from . import serializers


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Products
    template_name = 'product_list.html'
    context_object_name = 'products' # Contexto enviado para o template
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página
    permission_required = 'products.view_product'

    def get_queryset(self): # Método que faz filtros pelo nome da marca
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        serie_number = self.request.GET.get('serie_number')

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
        
        if title:
            queryset = queryset.filter(title__icontains=title)

        if category:
            queryset = queryset.filter(category__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Pegando o contexto original
        product_metrics = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = product_metrics
        return context
    

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Products
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list') # Em caso de sucesso, redireciona para a página de listagem
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Products
    template_name = 'product_detail.html'    
    permission_required = 'products.view_product'
    
    
class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Products
    template_name = 'product_update.html'   
    form_class = forms.ProductForm 
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'
    

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Products
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'
    
    
class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Products.objects.all()
    serializer_class = serializers.ProductSerializer