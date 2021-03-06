from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
	status = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = 'Status'

	def __unicode__(self):
		return self.status

class Notificador(models.Model):
	nombre = models.CharField(max_length=50)
	apePaterno = models.CharField(max_length=50, verbose_name="Apelido Paterno", null = True, blank = True)
	apeMaterno = models.CharField(max_length=50, verbose_name="Apelido Materno", null = True, blank = True)
	statusNotificador = models.ForeignKey(Status, verbose_name="Status")

	class Meta:
		verbose_name_plural = 'Notificadores'

	def __unicode__(self):
		return self.nombre

class Sitio(models.Model):
	lugar = models.CharField(max_length=255)
	referencia = models.TextField(max_length=255, null = True, blank = True)

	class Meta:
		verbose_name_plural = 'Sitios'

	def __unicode__(self):
		return self.lugar

class TipoServicio(models.Model):
	tipoServicio = models.CharField(max_length=255, verbose_name="Servicio")

	class Meta:
		verbose_name_plural = 'Tipos de Servicios'

	def __unicode__(self):
		return self.tipoServicio

class Ausencia(models.Model):
	noti = models.ForeignKey(Notificador, verbose_name='Notificador')
	motivo = models.ForeignKey(Status)
	fechaInicio = models.DateTimeField(auto_now_add=True)
	fechaFin = models.DateTimeField(auto_now_add=False, blank=True, null=True)

	def __unicode__(self):
		return unicode(self.id)

class Servicio(models.Model):
	solicitante = models.ForeignKey(User)
	notificador = models.ForeignKey(Notificador)
	fechaInicio = models.DateTimeField(auto_now_add=True)
	fechaEnterado = models.DateTimeField(auto_now_add=False, blank=True, null=True)
	fechaFin = models.DateTimeField(auto_now_add=False, blank=True, null=True)
	sitio = models.ManyToManyField(Sitio)
	actividad = models.ForeignKey(TipoServicio)
	comentarios = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Servicios'

	def __unicode__(self):
		return unicode(self.id)

report_builder_fieldsets = (
    ('Servicio', {
        'fields': ('solicitante', 'notificador', 'fechaInicio'),
    }),
)