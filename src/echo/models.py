from django.conf import settings
from django.db import models
from django.db.models import Model


class Echo(Model):
    data = models.JSONField(blank=True, null=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Echo"
        verbose_name_plural = "Echoes"
