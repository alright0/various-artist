from django.urls import path, re_path
from echo.views import EchoView

urlpatterns = [
    re_path("^echo/$", EchoView.as_view()),
]
