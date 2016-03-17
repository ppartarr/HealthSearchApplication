__author__ = 'Philippe'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','eHealth.settings')

import django
django.setup()

from eHealth.models import UserProfile, Category, Page

def populate():
    add_user(name="Bob",
             gender_choices='male',
             dateOfBirth="1978-06-23")

    add_user(name="Jen",
             gender_choices='female',
             dateOfBirth="1982-01-01")

    add_user(name="Jill",
             gender_choices='female',
             dateOfBirth="1956-09-01")

def add_user(name):
    u = UserProfile.objects.get_or_create()[0]
    u.save()
    return u