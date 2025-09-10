from django.db import models


# Modelo Tipo de Madera
class TipoMadera(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

# Modelo Cliente
class Cliente(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre_empresa

# Modelo Conductor
class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    licencia_conducir = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Modelo Camion
class Camion(models.Model):
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    capacidad_carga = models.FloatField(help_text="Capacidad en toneladas")
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE, related_name="camiones")

    def __str__(self):
        return f"{self.placa} - {self.modelo}"

# Modelo Carga
class Carga(models.Model):
    tipo_madera = models.ForeignKey(TipoMadera, on_delete=models.CASCADE, related_name="cargas")
    cantidad = models.FloatField(help_text="Cantidad en metros cúbicos")
    peso = models.FloatField(help_text="Peso en toneladas")
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE, related_name="cargas")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="cargas")

    def __str__(self):
        return f"Carga de {self.tipo_madera.nombre} para {self.cliente.nombre_empresa}"
