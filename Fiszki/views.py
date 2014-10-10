#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 28/9/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django.shortcuts import render, get_object_or_404, redirect

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

    if request.method == 'POST' and ret['form'].is_valid():
        ret['form'].save()
        redirect(home)
    return render(request, 'fiszki/add_category.html', ret)


def edit_fiszka(request, fiszka_id=None):
    """
    Function for adding or editing fiszka to app
    :param request:
    :return:
    """
    ret = {'form': FiszkaForm(request.POST or None)}

    if request.method == 'POST' and ret['form'].is_valid():
        ret['form'].save()

    return render(request, 'fiszki/add_fiszka.html', ret)


def delete_category(request):
    """
    Function for deleting category from app
    :param request:
    :return:
    """
    return render(request, 'fiszki/delete_category.html')


def delete_fiszka(request):
    """
    Function for deleting fiszka from app
    :param request:
    :return:
    """
    return render(request, 'fiszki/delete_fiszka.html')


def display_fiszka(request, fiszka_id):
    """
    Display fiszka with pk = fiszka_id
    :param request:
    :param fiszka_id:
    :return:
    """
    ret = {'fiszka': get_object_or_404(Fiszka, pk=fiszka_id)}

    return render(request, 'fiszki/display_fiszka.html', ret)


def about_author(request):
    """
    Display info about creator of this project
    :param request:
    :return:
    """
    return render(request, 'fiszki/about_author.html')
