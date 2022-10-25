from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet

from echo.models import Echo
from echo.serializers import EchoSerializer


class EchoView(ModelViewSet):
    queryset = Echo.objects.all()
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    serializer_class = EchoSerializer

    def post(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            request.user = None

        Echo.objects.create(data=request.data, user=request.user)
        return Response(request.data, status=status.HTTP_201_CREATED)
