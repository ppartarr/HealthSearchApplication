from django.conf.urls import patterns, url
from health_search.settings import STATIC_PATH
from eHealth import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       )
