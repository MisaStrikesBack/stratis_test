# -*- coding: utf-8 -*-
"""
Animals models
"""
from django.db import models
from django.core.validators import MinValueValidator

from stratis_web.constants import GENDER_OPTIONS


class Group(models.Model):
    """
    Animal food scheme
    """
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Species(models.Model):
    """
    Animal species model
    """
    name = models.CharField(max_length=60)
    scientific_name = models.CharField(max_length=80)
    group = models.ForeignKey(Group, related_name="species",
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_animals_number(self):
        return self.animals.all().count()


class Animal(models.Model):
    """
    Animal model
    """
    name = models.CharField(max_length=60)
    age = models.PositiveIntegerField(validators=[MinValueValidator(1), ])
    gender = models.CharField(max_length=4, choices=GENDER_OPTIONS)
    species = models.ForeignKey(Species, related_name="animals",
                                on_delete=models.CASCADE)
