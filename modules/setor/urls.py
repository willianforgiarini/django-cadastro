from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register(r'', views.SetorView, basename="setor")

urlpatterns = [
    path("", include(router.urls))
]
