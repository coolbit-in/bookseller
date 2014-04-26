from django.conf.urls import patterns, include, url
from bookseller import settings
# Uncomment the next two lines to enable the admin:
from bookseller.apps.main import views
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static

handle404 = 'bookseller.apps.main.http_errors_views.show_404_view'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookseller.views.home', name='home'),
    # url(r'^bookseller/', include('bookseller.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.show_index),
    url(r'^search/$', views.search),
    url(r'^item/', include('bookseller.apps.main.urls')),
    url(r'^account/', include('bookseller.apps.register.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/(.*)/(\d+)/$', 'bookseller.apps.register.views.list'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

