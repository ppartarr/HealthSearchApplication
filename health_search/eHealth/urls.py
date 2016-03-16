from django.conf.urls import patterns, url
from health_search.settings import STATIC_PATH
from eHealth import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^user/',views.user,name='user'),
                       url(r'^registertest/',views.register,name='user'),
                      #url(r'^user/(?P<user_name>[\w\-]+)/$',views.user,name='user'),
                       )
