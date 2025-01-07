from django.views.generic import ListView, CreateView, DetailView
from . import models, forms
from django.urls import reverse_lazy

class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página

    def get_queryset(self): # Método que faz filtros pelo nome da categoria
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    

class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list') # Em caso de sucesso, redireciona para a página de listagem


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'    