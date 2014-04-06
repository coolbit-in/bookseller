from django.conf.urls import patterns, url
from bookseller.apps.register import views

urlpatterns = patterns('',
    url(r'^(\d+)/$', views.account),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^errors/invalid_login/$', views.error_login_invalid)
)