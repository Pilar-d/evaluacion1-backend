from django.urls import path, include
from rest_framework import routers
from api import views
router = routers.DefaultRouter() 

router = routers.DefaultRouter()
router.register(r'tipos-madera', views.TipoMaderaViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'conductores', views.ConductorViewSet)
router.register(r'camiones', views.CamionViewSet)
router.register(r'cargas', views.CargaViewSet)


urlpatterns = [  
    path('', include(router.urls))

]

