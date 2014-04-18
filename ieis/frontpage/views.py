# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class Index(TemplateView):

    """ Front page """

    template_name = 'frontpage/index.html'
