# -*- coding: utf-8 -*-
from rest_framework import generics, permissions
from goods.models import *
from goods.serializers import *

class MainList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super(MainList, self).get_queryset()
        return queryset.order_by('?')[:9]

class TypeOfGoodsList(generics.ListAPIView):
    model = Type
    serializer_class = TypeSerializer

class GoodsOfTypeList(generics.ListAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super(GoodsOfTypeList, self).get_queryset()
        return queryset.filter(types__pk=self.kwargs.get('pk'))

class OneItem(generics.RetrieveAPIView):
    model = Item
    serializer_class = ItemSerializer
