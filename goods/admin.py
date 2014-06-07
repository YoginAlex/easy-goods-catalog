# -*- coding: utf-8 -*-
from django.contrib import admin
from goods.models import *

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Type)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_thumb',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_thumb', 'types', 'quantity', 'cost', 'show')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Item, ItemAdmin)
