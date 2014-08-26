# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from goods.views import *


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', IndexPage.as_view(), name="index-page"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('goods.urls'))
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

