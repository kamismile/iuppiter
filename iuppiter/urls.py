from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iuppiter.views.home', name='home'),
    # url(r'^iuppiter/', include('iuppiter.foo.urls')),
    url(r'^$', 'frontend.views.index',name="index"),
    url(r'^dream/',  include('frontend.urls')),
    url(r'^system/',  include('backend.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
