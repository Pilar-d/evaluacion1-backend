from django.contrib import admin
from .models import TipoMadera, Cliente, Conductor, Camion, Carga

# Registro de modelos en el panel de administración
# Evitamos duplicados usando una verificación
models_to_register = [TipoMadera, Cliente, Conductor, Camion, Carga]

for model in models_to_register:
    if not admin.site.is_registered(model):
        admin.site.register(model)
