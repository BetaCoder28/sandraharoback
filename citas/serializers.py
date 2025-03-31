from rest_framework import serializers
from service.serializers import ServiceSerializer  # Asegúrate de que el serializer de Service esté importado
from .models import Citas

class CitasSerializer(serializers.ModelSerializer):
    # Mostrar los nombres de los servicios relacionados
    servicio_nombres = serializers.SerializerMethodField()

    class Meta:
        model = Citas
        fields = ['id', 'date', 'schedule', 'servicios', 'usuario', 'servicio_nombres']

    def get_servicio_nombres(self, obj):
        # Devuelve una lista de nombres de los servicios relacionados
        return [service.service for service in obj.servicios.all()]

    # Si necesitas permitir crear citas con los IDs de los servicios:
    extra_kwargs = {
        'servicios': {'write_only': True}  # Usar el campo `servicios` para escribir los IDs
    }
