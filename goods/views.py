# -*- coding: utf-8 -*-
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = "base.html"
