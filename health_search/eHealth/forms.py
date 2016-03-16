from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    dateOfBirth = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'dateOfBirth', 'gender')
