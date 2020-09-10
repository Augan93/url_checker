from django.contrib import admin

from . import models


@admin.register(models.Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = (
        'text',
    )

