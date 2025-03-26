from rest_framework import viewsets
from .models import Citas
from .serializers import CitasSerializer

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all().select_related('servicio')
    serializer_class = CitasSerializer

    # Opcional: Filtrado por servicio
    def get_queryset(self):
        queryset = super().get_queryset()
        servicio_id = self.request.query_params.get('servicio')
        if servicio_id:
            queryset = queryset.filter(servicio__id=servicio_id)
        return queryset
