from django import forms

from .models import CotizaOficinas

class CotizaOficinasForm(forms.ModelForm):

    class Meta:
        model = CotizaOficinas
        fields = ('cve_corta', 'razon_social','consecutivo','observaciones')