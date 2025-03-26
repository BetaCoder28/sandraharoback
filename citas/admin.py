from django.contrib import admin
from .models import Citas

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'schedule', 'servicio')  # Incluye el campo relacionado
    list_filter = ('date', 'servicio')  # Filtros laterales
    search_fields = ('servicio__service',)  # Buscar por nombre de servicio