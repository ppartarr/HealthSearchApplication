from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from tango_with_django_project import  views
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/eHealth/'

urlpatterns = patterns('',