from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy

class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self): # Método que faz filtros pelo nome da marca
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class BrandCreateView(CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list') # Em caso de sucesso, redireciona para a página de listagem


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'    
    
    
class BrandUpdateView(UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'   
    form_class = forms.BrandForm 
    success_url = reverse_lazy('brand_list')
    

class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')