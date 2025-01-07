from django.views.generic import ListView, CreateView, DetailView
from . import models, forms
from django.urls import reverse_lazy

class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página

    def get_queryset(self): # Método que faz filtros pelo nome da categoria
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    

class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list') # Em caso de sucesso, redireciona para a página de listagem


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'    