from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile
from django.forms import extras
from django.core import validators



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    passwordAgain = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        passwordAgain = self.cleaned_data.get('passwordAgain')
        if password and passwordAgain:
            if password != passwordAgain:
                raise forms.ValidationError("The two password fields didn't match.")
        return passwordAgain

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
