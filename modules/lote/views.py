from django.contrib.gis.geos import GEOSGeometry

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from modules.zoneamento.models import Zoneamento
from modules.zoneamento.serializers import ZoneamentoSerializer
from modules.imobiliario.models import Imobiliario, ImobiliarioPessoa, ImobiliarioEdificacao
from modules.pessoa.models import Pessoa
from modules.pessoa.serializers import PessoaSerializer
from modules.edificacao.models import Edificacao
from modules.edificacao.serializers import EdificacaoSerializer
from utils.serializers.geom_serializer import PolygonSerializer

from .serializers import LoteSerializer
from .models import Lote


class LoteView(ModelViewSet):
    serializer_class = LoteSerializer
    queryset = Lote.objects.all().order_by("id")


    @extend_schema(
            responses=PessoaSerializer(many=True),
            description="Lista todos os propriétarios vinculados ao lote via Imobiliario"
    )
    @action(methods=["GET"], detail=True, url_path="proprietarios", pagination_class=None)
    def get_proprietarios_lote(self, request, pk):
        try:
            lote = self.get_object()
            
            imobiliarios = Imobiliario.objects.filter(lote=lote)
            imobiliario_pessoas = ImobiliarioPessoa.objects.filter(imobiliario__in=imobiliarios).values("pessoa")

            pessoas = Pessoa.objects.filter(id__in=imobiliario_pessoas)
            serializer = PessoaSerializer(pessoas, many=True)

            return Response(serializer.data)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @extend_schema(
            request=PolygonSerializer,
            responses=ZoneamentoSerializer(many=True),
            description="Lista zoneamentos a partir de um intersecção com uma geometria de lote"
    )
    @action(methods=["POST"], detail=False, url_path="intersects", pagination_class=None)
    def lote_intersect_zoneamento(self, request):
        try:
            serializer = PolygonSerializer(data=request.data)

            if serializer.is_valid():
                geom = serializer.validated_data.get("geom")

                queryset = Zoneamento.objects.filter(geom__intersects=geom)
                zoneamentos = ZoneamentoSerializer(queryset, many=True)

                return Response(zoneamentos.data)
        
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    @extend_schema(
            responses=EdificacaoSerializer(many=True),
            description="Lista as edificações de um lote"
    )
    @action(methods=["GET"], detail=True, url_path="edificacoes", pagination_class=None)
    def get_edificacoes_por_lote(self, request, pk):
        try:
            lote = self.get_object()
            imobiliarios = Imobiliario.objects.filter(lote=lote)
            imobiliario_edificacoes = ImobiliarioEdificacao.objects.filter(imobiliario__in=imobiliarios).values("edificacao")

            if not imobiliario_edificacoes:
                return Response({
                    "message": f"Lote ({pk}) não possui edificações."
                }, status=status.HTTP_404_NOT_FOUND)
                 
            edificacoes = Edificacao.objects.filter(id__in=imobiliario_edificacoes)
            serializer = EdificacaoSerializer(edificacoes, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
