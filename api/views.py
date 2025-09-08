from rest_framework import viewsets
from .models import TipoMadera, Cliente, Conductor, Camion, Carga
from .serializer import TipoMaderaSerializer, ClienteSerializer, ConductorSerializer, CamionSerializer, CargaSerializer

# ViewSets para cada modelo
class TipoMaderaViewSet(viewsets.ModelViewSet):
    queryset = TipoMadera.objects.all()
    serializer_class = TipoMaderaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class CamionViewSet(viewsets.ModelViewSet):
    queryset = Camion.objects.all()
    serializer_class = CamionSerializer

class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer


    
