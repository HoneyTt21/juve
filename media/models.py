from django.db import models
from core import models as core_models

# Create your models here.
class Media(core_models.AbstractTimeStamp):

    """Media Model"""

    name = models.CharField(max_length=30)
    url = models.URLField()
    short_name = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f"{self.name} ({self.short_name})"
