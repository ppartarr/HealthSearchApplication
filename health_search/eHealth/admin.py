from django.contrib import admin
from eHealth.models import UserProfile,Category, Page

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)

# Register your models here.
