from django.urls import re_path

from echo.views import EchoView

urlpatterns = [
    re_path("^echo/$", EchoView.as_view({"post": "post", "get": "list"})),
    re_path("^echo/<int:pk>/$", EchoView.as_view({"delete": "destroy"})),
]
