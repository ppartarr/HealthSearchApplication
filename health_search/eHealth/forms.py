from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile
from registration.forms import RegistrationForm
from django.forms import extras


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','dateOfBirth','gender')


class UserProfileFormTest(RegistrationForm):
    gender_choices=[('male','Male',),('female','Female',)]

    dateOfBirth=forms.DateField(widget=extras.SelectDateWidget)
    gender = forms.ChoiceField(choices=gender_choices)
    picture = forms.ImageField()
