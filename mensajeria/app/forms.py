from django import forms
from django.forms import ModelForm
from app.models import Servicio, Notificador

class ServicioForm(ModelForm):
	notificador = forms.ModelChoiceField(queryset=Notificador.objects.all().filter(statusNotificador=1))
	class Meta:
		model = Servicio
		exclude = ('solicitante', 'fechaEnterado', 'fechaFin')

class AusenciaForm(ModelForm):
	nombre = forms.ModelChoiceField(queryset=Notificador.objects.all())
	class Meta:
		model = Notificador
		exclude = ('apePaterno', 'apeMaterno',)
