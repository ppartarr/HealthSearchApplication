from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile, Page, Category
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

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


    class Meta:
        model = Page
        exclude = ('category','flesch_score','polarity_score','subjectivity_score','summary',)

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        exclude = ('user',)#todo not sure if i need this
        fields = ('name',)