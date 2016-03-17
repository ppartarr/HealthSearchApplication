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
    gender_choices=[('male','Male',),('female','Female',)]

    dateOfBirth=forms.DateField(widget=extras.SelectDateWidget)
    gender = forms.ChoiceField(choices=gender_choices)
    class Meta:
        model = UserProfile
        fields = ('dateOfBirth', 'gender','picture')
