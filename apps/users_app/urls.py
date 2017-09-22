from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/(?P<id>\d+)/change$', views.change),
    url(r'^create$', views.create),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^(?P<id>\d+)/edit$', views.edit),
    url(r'^new', views.new),
    url(r'^delete/(?P<id>\d+)$', views.delete)


]