from django.db.models import Sum

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from modules.imobiliario.models import Imobiliario

from .serializers import QuadraSerializer, AreaConstruidaPorQuadraSerializer
from .models import Quadra


class QuadraView(ModelViewSet):
    serializer_class = QuadraSerializer
    queryset = Quadra.objects.all().order_by("id")


@extend_schema(
        responses=AreaConstruidaPorQuadraSerializer(many=True),
        description="Retorna o total de area construida por quadra"
)
@api_view(["GET"])
def area_construida_por_quadra(request):
    """Retorna o total de area construida por quadra"""
    try:
        quadras = Quadra.objects.all()
        
        response = []
        for quadra in quadras:
            imobiliarios = Imobiliario.objects.filter(geom__intersects=quadra.geom).aggregate(
                area_construida=Sum("area_total_construida"),
            )

            imobiliarios["quadra"] = quadra.quadra
            imobiliarios["codigo"] = quadra.cod
            response.append(imobiliarios)

        return Response(response)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)