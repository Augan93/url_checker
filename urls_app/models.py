from django.db import models


class Url(models.Model):
    text = models.CharField(
        max_length=2000,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_paused = models.BooleanField(
        default=False,
    )
    status = models.IntegerField(
        null=True,
        blank=True,
    )
