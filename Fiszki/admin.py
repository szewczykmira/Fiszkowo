#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 2/10/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""
from django.contrib import admin
from .models import Category, Fiszka

admin.site.register(Category)
admin.site.register(Fiszka)
