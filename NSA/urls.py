__author__ = 'adamg_000'

from django.conf.urls import patterns, url
from NSA import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^map', views.map, name='map'),
    url(r'^event', views.event, name='event'),
)
