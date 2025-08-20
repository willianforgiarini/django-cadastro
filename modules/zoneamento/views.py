from django.db.models import Count

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from drf_spectacular.utils import extend_schema

from modules.lote.models import Lote

from .serializers import ZoneamentoSerializer, ZoneamentoUtilizacaoSerializer
from .models import Zoneamento


class ZoneamentoView(ModelViewSet):
    serializer_class = ZoneamentoSerializer
    queryset = Zoneamento.objects.all().order_by("id")

    @extend_schema(
            responses=ZoneamentoUtilizacaoSerializer(many=True),
            description="Para cada zoneamento, retorna a quatidade de lotes agrupados pelo campo utilizacao_terreo"
    )
    @action(methods=["GET"], detail=False, url_path="utilizacao-terreno", pagination_class=None)
    def get_utilizacao_terreno_por_zoneameto(self, request):
        try:
            zoneamentos = Zoneamento.objects.all()

            response = []
            for zona in zoneamentos:
                lotes = Lote.objects.filter(geom__intersects=zona.geom, utilizacao_terreno__isnull=False)
                agrupados = lotes.values("utilizacao_terreno").annotate(count=Count("id"))
                
                response.append({
                    "zona": zona.zona,
                    "utilizacoes": list(agrupados)
                })

            return Response(response)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)