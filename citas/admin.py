from django.contrib import admin
from .models import Citas

@admin.register(Citas)
class CitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'schedule')  # Mostrar los servicios en lugar de servicio
    list_filter = ('date',)  # Los servicios ya no se filtran directamente
    search_fields = ('servicios__service',)  # Buscar por nombre de servicio