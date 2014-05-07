from django import forms
from django.forms import ModelForm
from app.models import Servicio, Notificador, Ausencia, Sitio

class ServicioForm(ModelForm):
	notificador = forms.ModelChoiceField(queryset=Notificador.objects.all().filter(statusNotificador=1))
	sitio = forms.ModelMultipleChoiceField(queryset=Sitio.objects.all())
	class Meta:
		model = Servicio
		exclude = ('solicitante', 'fechaEnterado', 'fechaFin')

class AusenciaForm(ModelForm):
	class Meta:
		model = Ausencia
		exclude = ('fechaInicio', 'fechaFin',)
