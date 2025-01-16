import json
from django.shortcuts import render, redirect
from . import metrics
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User

@login_required(login_url='login')
def home(request):
      product_metrics = metrics.get_product_metrics()
      sales_metrics = metrics.get_sales_metrics()
      daily_sales_data = metrics.get_daily_sales_data()
      daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
      product_count_by_category = metrics.get_product_count_by_category()
      product_count_by_brand = metrics.get_product_count_by_brand()
      
      context = {
            'product_metrics': product_metrics,
            'sales_metrics': sales_metrics,
            'daily_sales_data': json.dumps(daily_sales_data), # Precisa converter para JSON pq o javascript não entende dicionário, apenas JSON
            'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
            'product_count_by_category': json.dumps(product_count_by_category),
            'product_count_by_brand': json.dumps(product_count_by_brand),
      }
      
      return render(request, 'home.html', context)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('choose_destination')  # Página de escolha para superusuários
            return redirect('home')  # Página do sistema para usuários comuns
        else:
            return render(request, 'registration/login.html', {'error': 'Usuário ou senha inválidos'})
      
    return render(request, 'registration/login.html')


@login_required(login_url='login')
def choose_destination(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redireciona usuários comuns para a página principal
    return render(request, 'choose_destination.html')

