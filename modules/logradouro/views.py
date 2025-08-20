from rest_framework.viewsets import ModelViewSet

from .serializers import LogradouroSerializer
from .models import Logradouro


class LogradouroView(ModelViewSet):
    serializer_class = LogradouroSerializer
    queryset = Logradouro.objects.all().order_by("id")