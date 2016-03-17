from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile
from django.forms import extras
from django.core import validators



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError("The two password fields didn't match.")
        return password2

    class Meta:
        model = User
        fields = ('username', 'email', 'password','password2')

class UserProfileForm(forms.ModelForm):
    gender_choices=[('male','Male',),('female','Female',)]

    dateOfBirth=forms.DateField(widget=extras.SelectDateWidget)
    gender = forms.ChoiceField(choices=gender_choices)
    class Meta:
        model = UserProfile
        fields = ('dateOfBirth', 'gender','picture')
