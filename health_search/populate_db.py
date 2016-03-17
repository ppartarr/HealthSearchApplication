__author__ = 'Philippe'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_search.settings')

import django
django.setup()

from django.contrib.auth.models import User

from eHealth.models import UserProfile, Category, Page

def populate():
    add_user(name="Bob",
             username="bobby",
             password="bob",
             email="bobby@bobby.com",
             gender_choices='male',
             dob="1978-06-23")

    add_user(name="Jen",
             username="Jenny",
             password="jen123",
             email="jen@hotmail.com",
             gender_choices='female',
             dob="1982-01-01")

    add_user(name="Jill",
             username="Jill",
             password="wordpass",
             email="jill@media.com",
             gender_choices='female',
             dob="1956-09-01")


def add_user(name, username, password, email, gender_choices, dob):
    user = User.objects.create_user(username, email, password)
    u = UserProfile.objects.get_or_create(user=user, gender=gender_choices, dateOfBirth=dob)[0]
    u.save()
    return u


if __name__ == '__main__':
    print "Starting the population script..."
    populate()
