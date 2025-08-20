from rest_framework.viewsets import ModelViewSet

from .serializers import PessoaSerializer
from .models import Pessoa


class PessoaView(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all().order_by("id")
    