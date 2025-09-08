from rest_framework import serializers
from .models import TipoMadera, Cliente, Conductor, Camion, Carga

class TipoMaderaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMadera
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class CamionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camion
        fields = '__all__'

class CargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carga
        fields = '__all__'
