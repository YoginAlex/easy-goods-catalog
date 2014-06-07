from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import patterns, url, include
from rest_framework import generics, permissions
from django.views.generic import TemplateView
from django.views.generic import ListView
from goods.serializers import *
from goods.models import *

class GoodsIndexPage(TemplateView):
    template_name = "base.html"

    # def head(self, *args, **kwargs):
    #     items = self.get_queryset().order_by('?')[:3]
    #     response = HttpResponse('')
    #     response['items'] = items

    #     return response

    def get_context_data(self, **kwargs):
        context = super(GoodsIndexPage, self).get_context_data(**kwargs)
        context['items'] = Item.objects.order_by('?')[:3]
        context['goods_types'] = Type.objects.all()
        return context

class GoodsOfTypeList(generics.ListAPIView):
    pass

class OneItem(generics.ListAPIView):
    pass