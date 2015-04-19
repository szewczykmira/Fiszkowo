#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 28/9/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse

from .models import Category, Fiszka
from .forms import CategoryForm, FiszkaForm
import json

def home(request):
    """
    Deflaut view for this app.
    :param request:
    :return:
    """
    ret = {'categories': Category.objects.all(),
           'form': CategoryForm()}
    return render(request, 'fiszki/home.html', ret)


def save_category(request):
    if request.method == 'POST' and request.is_ajax(): 
        form = CategoryForm(request.POST)
        cat = form.save()
        n_url = reverse('display_cat', kwargs={'cat_id': cat.id})
        return HttpResponse(json.dumps({'n_url': n_url, 'name': cat.name}), mimetype="application/json")
    return HttpResponseForbidden('Possible only by post ajax request')


def display_fiszka_for_category(request, cat_id):
    """
    :param request:
    :return:
    """
    ret = {'category': get_object_or_404(Category, pk=cat_id)}
    fiszka = ret['category'].fiszka_set.filter(is_known=False).order_by('?')
    if fiszka:
        ret['fiszka'] = fiszka[0]
    if request.method == 'POST':
        ret['fiszka'].is_known = True
        ret['fiszka'].save(update_fields=['is_known'])
        redirect('display_cat', cat_id=ret['category'].pk)
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
