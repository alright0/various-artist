from rest_framework import serializers

from echo.models import Echo


class EchoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Echo
        fields = '__all__'
