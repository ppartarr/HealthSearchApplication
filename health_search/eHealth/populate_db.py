__author__ = 'Philippe'
os.environ.setdefault('DJANGO_SETTINGS_MODULE','eHealth.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
