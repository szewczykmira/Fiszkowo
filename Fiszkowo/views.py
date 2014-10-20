#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 28/9/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    """
    Home view for project
    :param request: request object
    :return: template for home view
    """
    return render(request, 'home.html')
