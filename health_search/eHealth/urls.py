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
                       url(r'^goto/$', views.track_url, name='goto'),
                       url(r'^update_username/$', views.update_username, name='update_username'),
                       url(r'^update_email/$', views.update_email, name='update_email'),
                       url(r'^update_password/$', views.update_password, name='update_password'),
                       url(r'^update_picture/$', views.update_picture, name='update_picture'),
                       #url(r'^user/(?P<user_name>[\w\-]+)/$', views.user, name='user'),
                       )

from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )