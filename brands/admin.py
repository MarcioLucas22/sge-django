from django.contrib import admin
from . import models

# Altere o título exibido na aba do navegador
admin.site.site_title = "Controle de Estoque Admin"

# Altere o cabeçalho do painel de administração
admin.site.site_header = "Controle de Estoque - SGE"

# Altere o texto da página inicial do painel administrativo
admin.site.index_title = "Bem-vindo ao Painel Administrativo"

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)

admin.site.register(models.Brand, BrandAdmin)