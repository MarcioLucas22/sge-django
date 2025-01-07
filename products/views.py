from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = models.Products
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página

    def get_queryset(self): # Método que faz filtros pelo nome da marca
        queryset = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset
    

class ProductCreateView(CreateView):
    model = models.Products
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list') # Em caso de sucesso, redireciona para a página de listagem


class ProductDetailView(DetailView):
    model = models.Products
    template_name = 'product_detail.html'    
    
    
class ProductUpdateView(UpdateView):
    model = models.Products
    template_name = 'product_update.html'   
    form_class = forms.ProductForm 
    success_url = reverse_lazy('product_list')
    

class ProductDeleteView(DeleteView):
    model = models.Products
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')