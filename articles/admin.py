from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):

    """Article Admin"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("title", "description", "media")},
        ),
    )

    list_display = (
        "title",
        "description",
        "media",
    )
