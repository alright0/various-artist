from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView

from echo.models import Echo


class EchoView(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            request.user = None

        Echo.objects.create(data=request.data, user=request.user)
        return Response(request.data, status=status.HTTP_200_OK)
