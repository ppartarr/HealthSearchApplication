from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile
from django.forms import extras


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    gender_choices=(('1','male',),('2','female',))
    dateOfBirth=forms.DateTimeField(widget=extras.SelectDateWidget)
    gender = forms.CharField(widget=forms.RadioSelect)#,choices=gender_choices)
    class Meta:
        model = UserProfile
        fields = ('dateOfBirth', 'gender','picture')
