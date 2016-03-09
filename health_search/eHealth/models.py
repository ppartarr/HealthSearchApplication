from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    user = models.ForeignKey(UserProfile)
    name = models.Charfield(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    url = models.URLField()
    flesch_score = models.IntegerField(default=0)
    polarity_score = models.IntegerField(default=0)
    subjectivity_score = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

# Create your models here.
