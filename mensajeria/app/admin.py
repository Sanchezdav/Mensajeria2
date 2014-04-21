from django.contrib import admin
from app.models import *

class NotificadorAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apePaterno', 'apeMaterno', 'statusNotificador')

class ServicioAdmin(admin.ModelAdmin):
	list_display = ('id', 'solicitante', 'notificador', 'fechaInicio', 'fechaEnterado', 'fechaFin', 'actividad')
	raw_id_fields = ('solicitante',)
	list_filter = ('notificador', 'actividad', 'solicitante')
	search_fields = ('notificador__nombre', 'solicitante__username', 'sitio__lugar')

class StatusAdmin(admin.ModelAdmin):
	list_display = ("id", "status")

class AusenciaAdmin(admin.ModelAdmin):
	list_display = ('id','noti', 'motivo', 'fechaInicio', 'fechaFin')
	list_filter = ('noti', 'motivo')
	raw_id_fields = ('noti',)

admin.site.register(Status, StatusAdmin)
admin.site.register(Notificador, NotificadorAdmin)
admin.site.register(Sitio)
admin.site.register(TipoServicio)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Ausencia, AusenciaAdmin)
