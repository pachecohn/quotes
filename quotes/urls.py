from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^quotes/', include('webapp.urls', namespace='webapp')),
    url(r'^$', RedirectView.as_view(url='quotes'), name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
