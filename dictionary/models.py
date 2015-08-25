#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 20/10/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):
    """
    Class that defines article

    Fields:
    - article
    - definition
    """
    article = models.CharField(verbose_name=_('Article'),
            max_length=100,
            unique=True)
    definition = models.CharField(verbose_name=_('Definition'),
            max_length=300)
