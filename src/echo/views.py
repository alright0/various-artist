from rest_framework import authentication, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from echo.models import Echo
from echo.serializers import EchoSerializer


class EchoView(ModelViewSet):
    queryset = Echo.objects.all().order_by("-created")
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
        JWTAuthentication,
    )
    permission_classes = [IsAuthenticated]
    serializer_class = EchoSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            request.user = None

        Echo.objects.create(data=request.data, user=request.user)
        return Response(request.data, status=status.HTTP_201_CREATED)
