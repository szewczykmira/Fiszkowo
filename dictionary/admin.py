#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File created: 20/10/2014
author: Mira Szewczyk <szewczyk.mira@gmail.com>
"""
from django.contrib import admin
from .models import Article

admin.site.register(Article)