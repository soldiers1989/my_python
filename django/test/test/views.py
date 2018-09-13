# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    context = {}
    context['title'] = 'This is title!'
    context['body'] = 'This is body!'
    context['bottom'] = 'This is bottom!'
    return render(request, 'index.html', context)