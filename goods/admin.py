# -*- coding: utf-8 -*-
from django.contrib import admin
from goods.models import *

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Type)

def hide_from_site(modeladmin, request, queryset):
    queryset.update(show=False)
hide_from_site.short_description = u'Скрыть с сайта'

def show_on_site(modeladmin, request, queryset):
    queryset.update(show=True)
show_on_site.short_description = u'Показать на сайте'

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_thumb',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_thumb', 'types', 'quantity', 'cost', 'show')
    actions = [hide_from_site, show_on_site]

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Item, ItemAdmin)

