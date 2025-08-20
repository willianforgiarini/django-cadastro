from rest_framework.viewsets import ModelViewSet

from .serializers import EdificacaoSerializer
from .models import Edificacao


class EdificacaoView(ModelViewSet):
    serializer_class = EdificacaoSerializer
    queryset = Edificacao.objects.all().order_by("id")