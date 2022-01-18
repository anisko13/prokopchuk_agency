from django.contrib import admin

from team.models import Teammate


@admin.register(Teammate)
class TeammateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
