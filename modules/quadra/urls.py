from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'', views.QuadraView, basename="quadra")

urlpatterns = [
    path("area-construida/", views.area_construida_por_quadra, name="area-construida"),
    path("", include(router.urls))
]
