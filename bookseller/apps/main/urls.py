from django.conf.urls import patterns, url

from bookseller.apps.main import views
from bookseller.apps.register.views import account
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account/(\d+)/$', account)
)
