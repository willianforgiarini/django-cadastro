from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register(r'imobiliario', views.ImobiliarioView, basename="imobiliario")
router.register(r'imobiliario-pessoa', views.ImobiliarioPessoaView, basename="imobiliario-pessoa")
router.register(r'imobiliario-edificacao', views.ImobiliarioEdificacaoView, basename="imobiliario-edificacao")

urlpatterns = [
    path("imobiliario/proximos/", views.imobiliarios_proximos, name="imobiliarios-proximos"),
    path("", include(router.urls)),
]
