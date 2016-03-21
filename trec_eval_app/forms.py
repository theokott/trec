__author__ = '2131905K'
from django import forms
from django.contrib.auth.models import User
from trec_eval_app.models import Track, Task, Run, UserProfile, UploadedRun


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "username", "email", "password")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("university", "description", 'picture')

class UploadRunForm(forms.ModelForm):
    class Meta:
        model = UploadedRun
        fields = ("file",)
