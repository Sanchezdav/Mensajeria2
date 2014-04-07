from django import forms
from django.forms import ModelForm
from app.models import Servicio, Notificador, Ausencia

class ServicioForm(ModelForm):
	notificador = forms.ModelChoiceField(queryset=Notificador.objects.all().filter(statusNotificador=1))
	class Meta:
		model = Servicio
		exclude = ('solicitante', 'fechaEnterado', 'fechaFin')

class AusenciaForm(ModelForm):
	noti = forms.ModelChoiceField(queryset=Notificador.objects.all())
	class Meta:
		model = Ausencia
		exclude = ('fechaInicio', 'fechaFin',)
