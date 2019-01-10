# -*- coding: utf-8 -*-
"""
animals forms
"""
from django import forms

from stratis_web.models import Species, Animal


class SpeciesForm(forms.ModelForm):
    """
    Species model form
    """
    class Meta:
        model = Species
        fields = '__all__'


class AnimalForm(forms.ModelForm):
    """
    Species model form
    """
    class Meta:
        model = Animal
        fields = '__all__'
