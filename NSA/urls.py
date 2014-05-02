__author__ = 'adamg_000'

from django.conf.urls import patterns, url
from NSA import views

urlpatterns = patterns(
    '',
    url(r'^index', views.index, name='index'),
    url(r'^$', views.map, name='map'),
    url(r'^about', views.about, name='about'),
    url(r'^map', views.map, name='map'),
    url(r'^event', views.event, name='event'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
)
