# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import patterns, url, include
from rest_framework import generics, permissions
from django.views.generic import TemplateView
from goods.models import *

class GoodsIndexPage(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(GoodsIndexPage, self).get_context_data(**kwargs)
        context['items'] = Item.objects.order_by('?')[:3]
        context['goods_types'] = Type.objects.all()
        return context
