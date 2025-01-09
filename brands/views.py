from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class BrandListView(LoginRequiredMixin, ListView): # LoginRequiredMixin deve ser o primeiro atributo a ser passado na classe
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página

    def get_queryset(self): # Método que faz filtros pelo nome da marca
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class BrandCreateView(LoginRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list') # Em caso de sucesso, redireciona para a página de listagem


class BrandDetailView(LoginRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'    
    
    
class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'   
    form_class = forms.BrandForm 
    success_url = reverse_lazy('brand_list')
    

class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')