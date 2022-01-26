from django.contrib import admin

from main.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
