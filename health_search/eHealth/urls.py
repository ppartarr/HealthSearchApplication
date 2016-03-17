from django.conf.urls import patterns, url
from health_search.settings import STATIC_PATH
from eHealth import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^user/', views.user, name='user'),
                       url(r'^registertest/', views.register, name='registertest'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
                       # url(r'^user/(?P<user_name>[\w\-]+)/$',views.user,name='user'),
                       )
