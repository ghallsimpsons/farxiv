from django.conf.urls import patterns, include, url
from django.contrib import admin
import farxiv.urls

urlpatterns = patterns('',
    url(r'', include(farxiv.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('registration.backends.default.urls')),
)
