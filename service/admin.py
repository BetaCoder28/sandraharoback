from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service')  # Campos visibles en la lista
    search_fields = ('service',)  # Campos buscables