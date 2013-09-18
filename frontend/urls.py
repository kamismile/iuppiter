from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'frontend.views.home', name='home'),
    # url(r'^iuppiter/', include('iuppiter.foo.urls')),

)
