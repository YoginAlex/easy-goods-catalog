# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.db.models import Q
from goods.models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_thumb',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_thumb', 'types', 'quantity', 'cost', 'show', )

    def hide_from_site(modeladmin, request, queryset):
        queryset.update(show=False)
    hide_from_site.short_description = u'Скрыть с сайта'

    def show_on_site(modeladmin, request, queryset):
        queryset.update(show=True)
    show_on_site.short_description = u'Показать на сайте'

    actions = [hide_from_site, show_on_site, ]

    def hide_all_no_cost(self, request):
        self.model.objects.all().filter(Q(cost__lte=0) | Q(cost__isnull=True)).update(show=False)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    def hide_all_no_quantity(self, request):
        self.model.objects.all().filter(Q(quantity__lte=0) | Q(quantity__isnull=True)).update(show=False)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    def get_urls(self):
        urls = super(ItemAdmin, self).get_urls()
        my_urls = [
            url(r'^hide_all_no_cost/$', self.hide_all_no_cost),
            url(r'^hide_all_no_quantity/$', self.hide_all_no_quantity),
        ]
        return my_urls + urls

    change_list_buttons = [
        {
            'url': 'hide_all_no_cost',
            'textname': u'Скрыть все без цены',
            'confirm': u'Точно?',
        },
        {
            'url': 'hide_all_no_quantity',
            'textname': u'Скрыть все с 0 остатком',
            'confirm': u'Точно?',
        },
    ]

    def changelist_view(self, request, extra_context={}):
        extra_context['change_list_buttons'] = self.change_list_buttons
        return super(ItemAdmin, self).changelist_view(request, extra_context=extra_context)

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Item, ItemAdmin)

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Type)
