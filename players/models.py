from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# Create your models here.

class League(core_models.AbstractTimeStamp):

    """League Model"""
    name = models.CharField(max_length=30)
    country = CountryField()

    def __str__(self):
        return f'{self.name} ({self.country})'

class Club(core_models.AbstractTimeStamp):
    
    """Club Model"""

    name = models.CharField(max_length=30)
    league = models.ForeignKey(
        League, related_name="clubs", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name;

    class Meta:
        verbose_name_plural = "Clubs"


class Player(core_models.AbstractTimeStamp):
    
    """ Custom Player Model """

    first_name = models.CharField(max_length = 60)
    mid_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    county_born = models.CharField(max_length = 30)
    country_born = CountryField()
    nationality = CountryField(multiple = True)
    club = models.ForeignKey(
        Club, related_name="players", on_delete=models.CASCADE
    )
    back_number = models.IntegerField()
    birthday = models.DateField(default=None)

    def __str__(self):
        return self.first_name + self.last_name

    def save(self, *args, **kwargs):
        self.county_born = str.capitalize(self.county_born)
        self.first_name = str.capitalize(self.first_name)
        self.mid_name = str.capitalize(self.mid_name)
        self.last_name = str.capitalize(self.last_name)
        super().save(*args, **kwargs)