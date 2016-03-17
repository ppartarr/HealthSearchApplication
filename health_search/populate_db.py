__author__ = 'Philippe'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_search.settings')

import django
django.setup()

from eHealth.models import UserProfile, Category, Page

def populate():
    add_user(name="Bob",
             gender_choices='male',
             dob="1978-06-23")

    add_user(name="Jen",
             gender_choices='female',
             dob="1982-01-01")

    add_user(name="Jill",
             gender_choices='female',
             dob="1956-09-01")


def add_user(name, gender_choices, dob):
    u = UserProfile.objects.get_or_create(username=name, gender=gender_choices, dateOfBirth=dob)[0]
    u.save()
    return u


if __name__ == '__main__':
    print "Starting the population script..."
    populate()
