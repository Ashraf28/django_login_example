from django import forms
from django.contrib.auth.models import User
from myapp.models import UserProInf

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProFo(forms.ModelForm):
    class Meta():
        model = UserProInf
        fields = ('portfol_site', 'pro_pic')
