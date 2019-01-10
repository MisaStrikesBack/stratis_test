# -*- coding: utf-8 -*-
"""
Core views
"""
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """
    This view renders the propper dashboard
    """
    template_name = "stratis_web/dashboard.html"
