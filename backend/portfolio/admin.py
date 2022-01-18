from django.contrib import admin

from portfolio.models import PortfolioProject


@admin.register(PortfolioProject)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link']
