from rest_framework import viewsets
from .models import Citas
from .serializers import CitasSerializer

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer
