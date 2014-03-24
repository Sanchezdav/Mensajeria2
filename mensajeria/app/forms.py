from django import forms
from django.forms import ModelForm
from app.models import *

class ServicioForm(ModelForm):
	notificador = forms.ModelChoiceField(queryset=Notificador.objects.all().filter(statusNotificador=1))
	class Meta:
		model = Servicio
		exclude = ('solicitante', 'fechaEnterado', 'fechaFin')
