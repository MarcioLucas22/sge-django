from . import models
from django.contrib import admin

class OutflowAdmin(admin.ModelAdmin):
      list_display = ('product', 'quantity', 'created_at', 'updated_at')
      search_fields = ('product__title',)

admin.site.register(models.Outflow, OutflowAdmin)
