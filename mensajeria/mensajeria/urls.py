from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from app.views import *

urlpatterns = patterns('',
    

    url(r'^admin/', include(admin.site.urls)),
)
