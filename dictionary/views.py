#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 10/11/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

from .models import Article


def home(request):
    """
    Deflaut view for this app.
    :param request:
    :return:
    """
    return render(request, 'dictionary/home.html')
