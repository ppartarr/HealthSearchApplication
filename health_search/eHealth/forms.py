from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile
from django.forms import extras
#TODO fix or remove
#from registration.forms import RegistrationForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    gender_choices=[('male','Male',),('female','Female',)]
    ateOfBirth=forms.DateField(widget=extras.SelectDateWidget)
    #gender = forms.ChoiceField(choices=gender_choices)
    class Meta:
        model = UserProfile
        fields = ('picture','dateOfBirth','gender')

#TODO fix or remove
#class UserProfileFormTest(RegistrationForm):
    #gender_choices=[('male','Male',),('female','Female',)]

    #dateOfBirth=forms.DateField(widget=extras.SelectDateWidget)
    #gender = forms.ChoiceField(choices=gender_choices)
