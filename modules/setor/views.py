from rest_framework.viewsets import ModelViewSet

from .serializers import SetorSerializer
from .models import Setor


class SetorView(ModelViewSet):
    serializer_class = SetorSerializer
    queryset = Setor.objects.all().order_by("id")