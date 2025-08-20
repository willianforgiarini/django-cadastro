from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from drf_spectacular.utils import extend_schema

from modules.edificacao.models import Edificacao
from modules.edificacao.serializers import EdificacaoSerializer

from .serializers import BairroSerializer, EdificacoesPorBairro
from .models import Bairro


class BairroView(ModelViewSet):
    serializer_class = BairroSerializer
    queryset = Bairro.objects.all().order_by("id")


    @extend_schema(
            responses=EdificacoesPorBairro,
            description="Lista as edificações de um bairro em especifico"
    )
    @action(methods=["GET"], detail=True, url_path="edificacoes")
    def get_edificacoes_por_bairro(self, request, pk):
        try:
            bairro = self.get_object()

            edificacoes = Edificacao.objects.filter(geom__intersects=bairro.geom)
            serializer = EdificacaoSerializer(edificacoes, many=True)

            response = {
                "bairro": bairro.nome,
                "edificacoes": serializer.data
            }

            return Response(response)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)