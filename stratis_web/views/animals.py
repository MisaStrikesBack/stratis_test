# -*- coding: utf-8 -*-
"""
animals views
"""
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from stratis_web.models import Animal, Species


class SpeciesListMixin(ListView):
    model = Species
    context_object_name = "species"
    template_name = "stratis_web/animals/list.html"


class SpeciesListView(SpeciesListMixin):
    title = "Todos los animales"


class HerbListView(SpeciesListMixin):
    title = "Animales Herviboros"

    def get_queryset(self):
        return self.model.objects.filter(group=1)


class CarnListView(SpeciesListMixin):
    title = "Animales Carnivoros"

    def get_queryset(self):
        return self.model.objects.filter(group=2)


class SpeciesDetailView(DetailView):
    model = Species
    context_object_name = "species"
    template_name = "stratis_web/animals/species-details.html"

    def get_animals(self):
        return self.object.animals.all()


class AnimalDetailView(DetailView):
    model = Animal
    context_object_name = "animal"
    template_name = "stratis_web/animals/animal-details.html"
