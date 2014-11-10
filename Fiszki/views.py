#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 28/9/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

from .models import Category, Fiszka
from .forms import CategoryForm, FiszkaForm


def home(request):
    """
    Deflaut view for this app.
    :param request:
    :return:
    """

    ret = {}
    ret['categories'] = Category.objects.all()

    return render(request, 'fiszki/home.html', ret)


def add_category(request):
    """
    Function for adding categories to app
    :param request:
    :return:
    """
    ret = {'form': CategoryForm(request.POST or None)}

    if request.method == 'POST':
        if ret['form'].is_valid():
            ret['form'].save()
            return redirect(reverse('home'))
    return render(request, 'fiszki/add_category.html', ret)


def display_fiszka_for_category(request,cat_id):
    """

    :param request:
    :return:
    """
    ret = {'category': get_object_or_404(Category, pk=cat_id)}
    ret['fiszka'] = Fiszka.objects.filter(cat=ret['category']).order_by('?')[0]
    if request.method == 'POST':
        ret['fiszka'].is_known = True
        ret['fiszka'].save(update_fields=['is_known'])
    return render(request, 'fiszki/display_fiszka.html', ret)


def edit_fiszka(request):
    """
    Function for adding or editing fiszka to app
    :param request:
    :return:
    """
    ret = {'form': FiszkaForm(request.POST or None)}

    if request.method == 'POST':
        if ret['form'].is_valid():
            ret['form'].save()
            return redirect(reverse('home'))
    return render(request, 'fiszki/add_fiszka.html', ret)


def about_author(request):
    """
    Display info about creator of this project
    :param request:
    :return:
    """
    return render(request, 'fiszki/about_author.html')
