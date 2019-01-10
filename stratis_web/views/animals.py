# -*- coding: utf-8 -*-
"""
animals views
"""
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from stratis_web.models import Animal, Species
from stratis_web.forms import SpeciesForm, AnimalForm
from stratis_web.views.mixins import StaffRequiedMixin


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
    delete_target = 'web:species:delete'
    modal_title = "Especie"
    modal_message = (
        'Al borrar esta especie también se borraran los animales de la misma')

    def get_animals(self):
        return self.object.animals.all()


class SpeciesCreationView(StaffRequiedMixin, CreateView):
    title = "Nueva Especie"
    form_class = SpeciesForm
    success_url = reverse_lazy('web:species:all')
    template_name = "stratis_web/animals/creation.html"


class SpeciesUpdateView(StaffRequiedMixin, UpdateView):
    title = "Edición de Especie"
    model = Species
    form_class = SpeciesForm
    template_name = "stratis_web/animals/creation.html"

    def get_success_url(self):
        return reverse_lazy(
            'web:species:detail',
            kwargs={'pk': self.object.pk})


class SpeciesDeleteView(StaffRequiedMixin, DeleteView):
    model = Species
    success_url = reverse_lazy('web:species:all')


class AnimalDetailView(DetailView):
    model = Animal
    context_object_name = "animal"
    delete_target = 'web:species:animal-delete'
    modal_title = 'Ejemplar'
    template_name = "stratis_web/animals/animal-details.html"


class AnimalCreationView(StaffRequiedMixin, CreateView):
    title = "Nuevo Ejemplar"
    form_class = AnimalForm
    success_url = reverse_lazy('web:species:all')
    template_name = "stratis_web/animals/creation.html"


class AnimalUpdateView(StaffRequiedMixin, UpdateView):
    title = "Edición de Ejemplar"
    model = Animal
    form_class = AnimalForm
    template_name = "stratis_web/animals/creation.html"

    def get_success_url(self):
        return reverse_lazy(
            'web:species:animal-detail',
            kwargs={'pk': self.object.pk})


class AnimalDeleteView(StaffRequiedMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy('web:species:all')
