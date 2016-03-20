from django import forms
from django.contrib.auth.models import User
from eHealth.models import UserProfile, Page, Category
from django.forms import extras
from django.core import validators
import datetime

class UserForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(label='Email Adress')
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Retype your Password')

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

class UserEditNameForm(forms.ModelForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username',)

class UserEditEmailForm(forms.ModelForm):
    email = forms.EmailField(label='Email Adress')
    class Meta:
        model = User
        fields = ('email',)

class UserEditPasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Retype your Password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2:
            if password != password2:
                raise forms.ValidationError("The two password fields didn't match.")
        return password2

    class Meta:
        model = User
        fields = ('password','password2',)

class UserProfileForm(forms.ModelForm):
    gender_choices=[('male','Male',),('female','Female',)]
    #date range between this year and upto 120 (oldest a peson has lived is 116)
    current_year = datetime.date.today().year
    dateOfBirth=forms.DateField(widget=forms.extras.SelectDateWidget(years=[year for year in reversed(range(current_year-120,current_year))]),
                                label='Date of Birth')
    gender = forms.ChoiceField(choices=gender_choices)
    class Meta:
        model = UserProfile
        fields = ('dateOfBirth', 'gender','picture')

class UserEditPictureForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    summary = forms.CharField(max_length=1000,help_text='Please enter a page summary.')
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
        exclude = ('category','flesch_score','polarity_score','subjectivity_score',)



class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    public = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        exclude = ('user',)
        fields = ('name',)
