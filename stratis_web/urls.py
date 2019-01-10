# -*- coding: utf-8 -*-
"""
stratis_web urls
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views

from stratis_web.views import (
    DashboardView, SpeciesListView, HerbListView, CarnListView,
    SpeciesDetailView, AnimalDetailView)

app_name = "stratis_web"

auth_patterns = ([
    path('login/',
         auth_views.LoginView.as_view(
             template_name='stratis_web/auth/login.html',
             redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
], 'auth')

animals_patterns = ([
    path('all/', SpeciesListView.as_view(), name='all'),
    path('herbivorous/', HerbListView.as_view(), name='herbs'),
    path('carnivorous/', CarnListView.as_view(), name='carns'),
    path('<int:pk>/', SpeciesDetailView.as_view(), name='detail'),
    path('animal/<int:pk>/', AnimalDetailView.as_view(),
         name='animal-detail'),
], 'species')

urlpatterns = [
    path('auth/', include(auth_patterns)),
    path('', DashboardView.as_view(), name="dashboard"),
    path('species/', include(animals_patterns)),
]
