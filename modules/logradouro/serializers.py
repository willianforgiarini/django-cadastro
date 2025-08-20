from rest_framework import serializers
from .models import Logradouro


class LogradouroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logradouro
        fields = "__all__"