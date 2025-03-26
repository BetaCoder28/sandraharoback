from rest_framework import serializers
from service.serializers import ServiceSerializer
from .models import Citas


class CitasSerializer(serializers.ModelSerializer):
    # Muestra el nombre del servicio en lugar del ID (opcional)
    servicio_nombre = serializers.CharField(source='servicio.service', read_only=True)
    
    class Meta:
        model = Citas
        fields = ['id', 'date', 'schedule', 'servicio', 'servicio_nombre']
        # Si quieres permitir crear citas con el ID del servicio:
        extra_kwargs = {
            'servicio': {'write_only': True}
        }

# Opcional: Si prefieres nested relationships
class CitasNestedSerializer(serializers.ModelSerializer):
    servicio = ServiceSerializer(read_only=True)
    
    class Meta:
        model = Citas
        fields = ['id', 'date', 'schedule', 'servicio']