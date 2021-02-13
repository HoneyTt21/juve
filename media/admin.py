from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):

    """Media Admin"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "short_name", "url")},
        ),
    )
