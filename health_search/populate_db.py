__author__ = 'Philippe'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_search.settings')

import django
django.setup()

from django.contrib.auth.models import User

from eHealth.models import UserProfile, Category, Page

def populate():
    user=add_user(name="Bob",
             username="bob",
             password="bob",
             email="bobby@bobby.com",
             gender_choices='male',
             dob="1978-06-23")

    cat=add_category(user=user,
                 name="Bob's public cat",
                 views=20,
                 public=True)

    add_page(cat=cat,
             title='Django Basics',
             url='http://www.tangowithdjango.com/book17/chapters/setup.html',
             views=20)

    cat=add_category(user=user,
                 name="Bob' bobs private cat",
                 views=30,
                 public=False)

    add_page(cat=cat,
             title='Getting Ready to Tango',
             url='http://www.tangowithdjango.com/book17/chapters/requirements.html',
             views=30)

    cat=add_category(user=user,
                 name="The cure to baldness?",
                 views=253,
                 public=True)

    add_page(cat=cat,
             title='Hair loss',
             url='http://en.wikipedia.org/wiki/Hair_loss',
             views=150)

    add_page(cat=cat,
             title='telegraph on baldness',
             url='http://www.telegraph.co.uk/men/health/how-to-cure-baldness-without-losing-your-money-as-well-as-your-h/',
             views=100)

    add_page(cat=cat,
             title='Pattern Baldness',
             url='http://www.mensfitness.com/styleandgrooming/fashion/your-diabolical-follicles-treating-male-pattern-baldness',
             views=3)



    user=add_user(name="Jen",
             username="jen",
             password="jen",
             email="jen@hotmail.com",
             gender_choices='female',
             dob="1982-01-01")

    cat=add_category(user=user,
                 name="Help with chemo",
                 views=120,
                 public=True)

    add_page(cat=cat,
             title='Chemotherapy NHS',
             url='http://www.nhs.uk/conditions/Chemotherapy/Pages/Definition.aspx',
             views=70)

    add_page(cat=cat,
             title='medlineplus advice',
             url='http://www.nlm.nih.gov/medlineplus/cancerchemotherapy.html',
             views=50)

    cat=add_category(user=user,
                 name="Wills, and other family stuff",
                 views=10,
                 public=False)

    add_page(cat=cat,
             title='Templates and Static Media',
             url='http://www.tangowithdjango.com/book17/chapters/templates_static.html',
             views=10)




    user=add_user(name="Jill",
             username="jill",
             password="jill",
             email="jill@media.com",
             gender_choices='female',
             dob="1956-09-01")

    cat=add_category(user=user,
                 name="What is the flu?",
                 views=185,
                 public=True)

    add_page(cat=cat,
             title='Models and Databases',
             url='http://www.tangowithdjango.com/book17/chapters/models.html',
             views=100)

    add_page(cat=cat,
             title='Models, Templates and Views',
             url='http://www.tangowithdjango.com/book17/chapters/models_templates.html',
             views=80)
    add_page(cat=cat,
             title='Overview',
             url='http://www.tangowithdjango.com/book17/chapters/overview.html',
             views=80)



def add_user(name, username, password, email, gender_choices, dob):
    user = User.objects.create_user(username, email, password)
    u = UserProfile.objects.get_or_create(user=user, gender=gender_choices, dateOfBirth=dob)[0]
    u.save()
    return u


def add_category(user,name,views,public):
    cat = Category.objects.get_or_create(user=user,name=name, views=views,public=public)[0]
    cat.save()
    return cat

def add_page(cat,title,url,views=0):
    summary='Added via populate'
    page= Page.objects.get_or_create(category=cat,title=title,url=url,views=views,summary=summary)[0]
    page.get_scores()

if __name__ == '__main__':
    print "Starting the population script..."
    populate()
