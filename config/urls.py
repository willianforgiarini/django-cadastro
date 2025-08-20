from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),

    path("admin/", admin.site.urls),
    path("bairro/", include("modules.bairro.urls")),
    path("edificacao/", include("modules.edificacao.urls")),
    path("", include("modules.imobiliario.urls")),
    path("logradouro/", include("modules.logradouro.urls")),
    path("lote/", include("modules.lote.urls")),
    path("pessoa/", include("modules.pessoa.urls")),
    path("quadra/", include("modules.quadra.urls")),
    path("setor/", include("modules.setor.urls")),
    path("zoneamento/", include("modules.zoneamento.urls")),
]
