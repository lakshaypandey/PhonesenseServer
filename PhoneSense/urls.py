from django.conf.urls import patterns, include, url

from PhoneSense.TrackServer.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^init$',init),
    url(r'^register$',register),
    url(r'^submit$',NewDataCollection),
    url(r'^handshake$',Handshake),
    url(r'^upload$',FileUpload),
    url(r'^get$',API),
    url(r'^source$',source),
    url(r'^documentation$',documentation),
    # url(r'^LocTrack/', include('LocTrack.LocTrack.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
