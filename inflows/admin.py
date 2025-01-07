from . import models
from django.contrib import admin

class InflowAdmin(admin.ModelAdmin):
      list_display = ('product', 'quantity', 'created_at', 'supplier', 'updated_at')
      search_fields = ('product__title', 'supplier__name')

admin.site.register(models.Inflow, InflowAdmin)
