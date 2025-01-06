from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy

class CategoryListView(ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página

    def get_queryset(self): # Método que faz filtros pelo nome da categoria
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    

class CategoryCreateView(CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list') # Em caso de sucesso, redireciona para a página de listagem


class CategoryDetailView(DetailView):
    model = models.Category
    template_name = 'category_detail.html'    
    
    
class CategoryUpdateView(UpdateView):
    model = models.Category
    template_name = 'category_update.html'   
    form_class = forms.CategoryForm 
    success_url = reverse_lazy('category_list')
    

class CategoryDeleteView(DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')