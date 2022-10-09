from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from echo.models import Echo


class EchoView(APIView):
    authentication_classes = [TokenAuthentication, BasicAuthentication]

    def post(self, request, *args, **kwargs):

        Echo.objects.create(data=request.data, user=request.user)
        return Response(request.data, status=status.HTTP_200_OK)
