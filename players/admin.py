from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):

    """League Admin"""

    fieldsets = (
        (
            "Info",
            {"fields": ("name", "country")},
        ),
    )

    list_display = (
        "name",
        "country",
        "count_clubs"
    )

    ordering = ("country", "name")

    list_filter = (
        "country",
    )

    search_fields = ("name", "country")

    def count_clubs(self, obj):
        return obj.clubs.count()

@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):

    """Club Admin"""

    fieldsets = (
        (
            "Info",
            {"fields": ("name", "league")},
        ),
    )

    list_display = (
        "name",
        "league",
        "count_players"
    )

    ordering = ("league", "name")

    list_filter = (
        "league",
    )

    search_fields = ("name", "league")

    def count_players(self, obj):
        return obj.players.count()

@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):

    """Player Admin"""

    fieldsets = (
        (
            "Name", 
            {"fields": ("first_name", "mid_name", "last_name")}
        ),
        (
            "Born", 
            {"fields": ("county_born", "country_born", "birthday")}
        ),
        (
            "Club",
            {"fields": ("club", "back_number")},
        ),
        (
            "Nationailty",
            {"fields": ("nationality",)}
        )
    )

    list_display = (
        "first_name",
        "last_name",
        "club",
        "back_number"
    )

    ordering = ("club", "back_number")

    list_filter = (
        "club",
        "nationality",
    )

    search_fields = ("name", "club", "nationality")
