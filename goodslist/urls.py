# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from goods.views import *

admin.autodiscover()

urlpatterns = patterns('',  
    url(r'^$', GoodsIndexPage.as_view(), name="index-page"),

    url(r'^goods_type/(?P<pk>\d+)$', GoodsOfTypeList.as_view(), name='goods-type-list'),
    url(r'^oneitem/(?P<pk>\d+)$', OneItem.as_view(), name='one-item'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

