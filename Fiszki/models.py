#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 27/9/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    """
    Category for every fiszka.
    """
    name = models.CharField(max_length=70, verbose_name=_('Category'), unique=True)

    def __unicode__(self):
        return self.name

class Fiszka(models.Model):
    """
    Definition of a model of fiszka.
    """

    name = models.CharField(max_length=50, verbose_name=_('Name'))
    definition = models.TextField(verbose_name=_('Definition'))
    is_known = models.BooleanField(default=False, verbose_name=_('Is known.'))
    cat = models.ForeignKey(Category, verbose_name=_('Category'), null=True)

    def __unicode__(self):
        return self.name
