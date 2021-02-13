from django.db import models
from media import models as media_models
from core import models as core_models

# Create your models here.


class ArticleImage(core_models.AbstractTimeStamp):
    """ Article Image Model """

    url = models.URLField()


class Article(core_models.AbstractTimeStamp):

    """Article Model"""

    title = models.CharField(max_length=30)
    description = models.TextField()
    media = models.ForeignKey(
        media_models.Media, related_name="media", on_delete=models.CASCADE
    )
    photo = models.ManyToManyField("ArticleImage")

    def __str__(self):
        return f"{self.title} / ({self.media})"
