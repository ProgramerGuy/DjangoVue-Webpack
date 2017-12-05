from django import forms
from django.forms import TextInput

from .models import CotizaOficinas

class CotizaOficinasForm(forms.ModelForm):

	class Meta:
		model = CotizaOficinas
		fields = ('cve_corta', 'razon_social','consecutivo','observaciones')
		widgets = {
			'cve_corta': TextInput(attrs={'v-model': 'data.cve_corta'}),
			'razon_social': TextInput(attrs={'v-model': 'data.razon_social'}),
			'consecutivo': TextInput(attrs={'v-model': 'data.consecutivo'}),
			'observaciones': TextInput(attrs={'v-model': 'data.observaciones'}),
			}

class FormsModel(forms.ModelForm):


	def __init__(self,model, params, *args, **kwargs):
		super(FormsModel, self).__init__(*args, **kwargs)
		print(model)
		print(params)
		self.meta.fields = self.params
		self.meta.model = self.model
