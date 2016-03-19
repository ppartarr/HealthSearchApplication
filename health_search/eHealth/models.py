from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from scores.scores import get_all_scores

class UserProfile(models.Model):
    def picname(self, *args, **kwargs):
        username = self.user.get_username()
        return 'profile_images/'+username

    gender_choices=(('male','Male',),('female','Female',))
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to=picname, blank=True)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6,choices=gender_choices)


    def __unicode__(self):
        return self.user.username




class Category(models.Model):
    user = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField()
    public = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def change_public(self,makepublic):
        self.public=makepublic

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    url = models.URLField()
    views = models.IntegerField(default=0)
    flesch_score = models.IntegerField(default=0)
    polarity_score = models.IntegerField(default=0)
    subjectivity_score = models.IntegerField(default=0)

    #todo check
    def save(self, *args, **kwargs):
        page_scores=get_all_scores(self.url)
        self.flesch_score       = page_scores[0]
        self.polarity_score     = page_scores[1]
        self.subjectivity_score = page_scores[2]
        super(Page, self).save(*args, **kwargs)
        #todo add summary

    def __unicode__(self):
        return self.title

# Create your models here.
