from . import models
from django.contrib import admin

class InflowAdmin(admin.ModelAdmin):
      list_display = ('name', 'description',)
      search_fields = ('name',)

admin.site.register(models.Supplier, InflowAdmin)
