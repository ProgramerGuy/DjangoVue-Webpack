# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import CotizaOficinasForm, FormsModel
from .models import CotizaOficinas
from django.shortcuts import redirect
from django.http import JsonResponse
from django.core import serializers
from django import forms
import json

def modelForm(model, fields):
	meta = type('Meta', (), { "model":model, "fields": fields })
	modelform_class = type("{0}Form".format(model.__name__), (forms.ModelForm,), {"Meta": meta})
	return modelform_class

def index(request):
	form = CotizaOficinasForm()
	form2 = modelForm(CotizaOficinas,['cve_corta','razon_social'])
	
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
		'form': form,
		'form2': form2,
	}
	return render(request, 'spa.html', context)

def oficinas(request):
	oficinas = CotizaOficinas.objects.all()
	print(oficinas)
	json = serializers.serialize("json",oficinas)
	return JsonResponse(json,safe=False)

def create(request):
	print(json.loads(request.body))
	CotizaOficinas.objects.create(**json.loads(request.body))
	form = CotizaOficinasForm(request.POST)
	ja = "holi"
	return JsonResponse(ja,safe=False)
