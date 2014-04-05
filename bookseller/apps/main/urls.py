from django.conf.urls import patterns, url

from bookseller.apps.main import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
