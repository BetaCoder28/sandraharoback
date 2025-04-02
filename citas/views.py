from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Citas
from .serializers import CitasSerializer

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

    def create(self, request, *args, **kwargs):
        print("Datos recibidos en la solicitud:", request.data)  # 👀 Ver datos en la consola
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
