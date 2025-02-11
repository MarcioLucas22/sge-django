from rest_framework import generics, serializers
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import serializers

class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView): # LoginRequiredMixin deve ser o primeiro atributo a ser passado na classe
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página
    permission_required = 'brands.view_brand' # Padrão colocar o nome da app (brands), qual a ação (add, change, delete ou view) e em seguida o nome da model (brand)

    def get_queryset(self): # Método que faz filtros pelo nome da marca
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list') # Em caso de sucesso, redireciona para a página de listagem
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'  
    permission_required = 'brands.view_brand'  
    
    
class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'   
    form_class = forms.BrandForm 
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.change_brand'
    

class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
    permission_required = 'brands.delete_brand'
    
class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    
class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer