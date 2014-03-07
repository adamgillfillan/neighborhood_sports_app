__author__ = 'adamg_000'

from django.conf.urls import patterns, url
from nsa import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
)