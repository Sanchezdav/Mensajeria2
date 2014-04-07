from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from app.views import *

urlpatterns = patterns('',
    url(r'^$', 'app.views.listing', name='notificadores'),
    url(r'^listaNoti/$', 'app.views.listingAusencia', name='listNoti'),
    url(r'^listaNoti/ausencias/$', Ausencias.as_view(), name='ausencias'),
    url(r'^finalizarAusencia/(?P<id_ausencia>\d+)$','app.views.finalizarAusencia', name='finalizarAusencia'),
    url(r'^servicios/$', ServiciosForm.as_view(), name='servicios'),
    url(r'^pendientes/$', 'app.views.pendientes', name='pendientes'),
    url(r'^enterado/(?P<id_servicio>\d+)$','app.views.enterado'),
    url(r'^finalizar/(?P<id_servicio>\d+)$','app.views.finalizar', name='finalizar'),
    url(r'^ingresar/$', 'django.contrib.auth.views.login', {'template_name':'login.html'},name='login'),
    url(r'^salir/$', 'django.contrib.auth.views.logout_then_login',name='logout'),

    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^table/$', 'app.views.listingTable', name='table'),

    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
