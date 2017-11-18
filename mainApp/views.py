# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {
        'msg': "randomly picked images",
        'user': request.user,
    }
    return render(request, 'spa.html', context)
