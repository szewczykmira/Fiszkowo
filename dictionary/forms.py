#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 10/11/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Article

class ArticleForm(forms.ModelForm):
    """
    form for creating instance for article class
    """

    article = forms.CharField(label=_('Article'),
                              required=True,
                              widget=forms.TextInput(attrs={'placeholder':
                                  _('Article'),
                                  'class': 'form-control'}))
    definition = forms.CharField(label=_('Definition'),
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':
                                     _('Definition'),
                                     'class': 'form-control'}))

    class Meta:
        model = Article
