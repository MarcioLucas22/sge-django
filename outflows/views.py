from django.views.generic import ListView, CreateView, DetailView
from . import models, forms
from django.urls import reverse_lazy
import app.metrics as metrics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from . import serializers

class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10 # Define a quantidade de elementos que serão exibidos por página
    permission_required = 'outflows.view_outflow'

    def get_queryset(self): # Método que faz filtros pelo nome da categoria
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Pegando o contexto original
        sales_metrics = metrics.get_sales_metrics()
        context['sales_metrics'] = sales_metrics
        return context
    

class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list') # Em caso de sucesso, redireciona para a página de listagem
    permission_required = 'outflows.add_outflow'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'    
    permission_required = 'outflows.view_outflow'
    

class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer
    
class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer