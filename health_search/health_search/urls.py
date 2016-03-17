from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from eHealth.forms import UserProfileFormTest

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'health_search.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('eHealth.urls')),
                       url(r'^accounts/register/$', RegistrationView.as_view(form_class=UserProfileFormTest)),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       )
