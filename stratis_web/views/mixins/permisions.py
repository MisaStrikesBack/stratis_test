# -*- coding: utf-8 -*-
"""
Mixins to handle group permission
"""
from django.shortcuts import redirect


class StaffRequiedMixin(object):
    """
    This mixin redirects all non staff users accessing the view
    """
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect('web:dashboard')
