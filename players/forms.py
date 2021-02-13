from django import forms
from django.forms import ModelForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from . import models


class AddPlayerForm(ModelForm):

    """Player Add Form"""

    class Meta:
        model = models.Player
        fields = [
            "first_name",
            "mid_name",
            "last_name",
            "county_born",
            "country_born",
            "club",
            "back_number",
            "birthday",
        ]

    def save(self, *args, **kwargs):
        player = super(AddPlayerForm, self).save(commit=False)
        player.save()
        return player