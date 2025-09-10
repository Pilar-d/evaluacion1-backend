from django.contrib import admin
from .models import TipoMadera, Cliente, Conductor, Camion, Carga

models_to_register = [TipoMadera, Cliente, Conductor, Camion, Carga]

for model in models_to_register:
    if not admin.site.is_registered(model):
        admin.site.register(model)
