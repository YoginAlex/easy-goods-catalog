# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from goods.views import *
from goods.api import *

urlpatterns = patterns('',
    url(r'^type_list/$', TypeOfGoodsList.as_view(), name="type-list"),
    url(r'^goods_type/(?P<pk>\d+)$', GoodsOfTypeList.as_view(), name='goods-type-list'),
    url(r'^oneitem/(?P<pk>\d+)$', OneItem.as_view(), name='one-item'),
    url(r'^main_list/$', MainList.as_view(), name='main-list'),
)