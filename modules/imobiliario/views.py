from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter

from utils.serializers.geom_serializer import PointSerializer


from .serializers import (
    ImobiliarioSerializer,
    ImobiliarioPessoaSerializer,
    ImobiliarioEdificacaoSerializer
)
from .models import (
    Imobiliario,
    ImobiliarioPessoa,
    ImobiliarioEdificacao
)


class ImobiliarioView(ModelViewSet):
    serializer_class = ImobiliarioSerializer
    queryset = Imobiliario.objects.all().order_by("id")


class ImobiliarioPessoaView(ModelViewSet):
    serializer_class = ImobiliarioPessoaSerializer
    queryset = ImobiliarioPessoa.objects.all().order_by("id")


class ImobiliarioEdificacaoView(ModelViewSet):
    serializer_class = ImobiliarioEdificacaoSerializer
    queryset = ImobiliarioEdificacao.objects.all().order_by("id")
    

@extend_schema(
        responses=ImobiliarioSerializer(many=True),
        parameters=[PointSerializer],
        description="Lista imobiliarios dentro de um raio a partir de uma localização"
)
@api_view(["GET"])
def imobiliarios_proximos(request):
    try:
        query_params = request.GET.dict()
        
        raio = float(query_params.get("raio"))
        serializer = PointSerializer(data=query_params)

        if serializer.is_valid():
            point = serializer.validated_data.get("point")
            point.srid = 4326

            imobiliarios = Imobiliario.objects.annotate(
                distancia=Distance('geom', point)
            ).filter(distancia__lte=D(m=raio)).order_by("distancia")

            if not imobiliarios:
                return Response({"message": "Nem um imobiliario encontrado nas proximidades"})

            serializer = ImobiliarioSerializer(imobiliarios, many=True)

            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)