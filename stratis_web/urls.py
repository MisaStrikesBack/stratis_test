# -*- coding: utf-8 -*-
"""
stratis_web urls
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views

from stratis_web.views import DashboardView

app_name = "stratis_web"

auth_patterns = ([
    path('login/',
         auth_views.LoginView.as_view(
             template_name='stratis_web/auth/login.html',
             redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
], 'auth')

urlpatterns = [
    path('auth/', include(auth_patterns)),
    path('', DashboardView.as_view(), name="dashboard"),
]
