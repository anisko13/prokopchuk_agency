from django.contrib import admin

from main.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']


@admin.register(HeaderSlide)
class HeaderSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(ServiceFooter)
class ServiceFooterAdmin(SummernoteModelAdmin):
    list_display = ['name', 'description']
    summernote_fields = ['description']


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title']
