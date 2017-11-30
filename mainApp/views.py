# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import CotizaOficinasForm
from django.shortcuts import redirect


def index(request):
	form = CotizaOficinasForm()
	if request.method == "POST":
		form = CotizaOficinasForm(request.POST)
		if form.is_valid():
		    post = form.save(commit=False)
		    post.save()
		    return redirect('/', pk=post.pk)
		else:
			form = CotizaOficinasForm()
	context = {
		'msg': "randomly picked images",
		'user': request.user,
		'form': form
	}
	return render(request, 'spa.html', context)
