#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 2/10/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Category, Fiszka

class CategoryForm(forms.ModelForm):
    """
    form for creating instance for category class
    """

    name = forms.CharField(label=_('Name'),
                           widget=forms.TextInput(attrs={'placeholder':
                               _('Name'), 'class':'form-control'}),
                           required=True)

    class Meta:
        model = Category

class FiszkaForm(forms.ModelForm):
    """
    form for creating instance for fiszka class
    """
    name = forms.CharField(label=_('Name'),
                           widget=forms.TextInput(attrs={'placeholder':
                               _('Name'), 'class': 'form-control'}),
                           required=True)
    definition = forms.CharField(label=_('Definition'),
                                 widget=forms.Textarea(attrs={'placeholder':
                                     _('Definition')}),
                                 required=True)
    is_known = forms.BooleanField(label=_('Is known'),
                                  required=False,
                                  initial=False,
                                  widget=forms.HiddenInput())
    cat = forms.ModelChoiceField(label=_('Category'),
                                 required=False,
                                 queryset=(Category.objects.all()),
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Fiszka
