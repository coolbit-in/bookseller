from django.conf.urls import patterns, url

from bookseller.apps.main import views
urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
   # url(r'^$', views.ItemList.as_view(), name='item_list'),
    url(r'^create/$', views.create, name='item_create'),
    url(r'^update/(?P<pk>\d+)/', views.update, name='item_update'),
    url(r'^view/(?P<pk>\d+)/', views.detail, name='item_detail'),
    url(r'^delete/(?P<pk>\d+)/', views.delete, name='item_delete'),
)