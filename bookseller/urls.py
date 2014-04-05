from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookseller.views.home', name='home'),
    # url(r'^bookseller/', include('bookseller.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', include('bookseller.apps.main.urls')),
    url(r'^item/', include('bookseller.apps.main.urls')),
    url(r'^register/$', 'bookseller.apps.register.views.register'),
    url(r'^errors/invalid_login/$', 'bookseller.apps.register.views.error_login_invalid'),
    url(r'^admin/', include(admin.site.urls)),
)

