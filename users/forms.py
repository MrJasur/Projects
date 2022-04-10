from dataclasses import field
from pyexpat import model
from django import forms
from .models import CustomUserModel

class UserCreationForm(forms.ModelForm):
    class Meta:
        model=CustomUserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name', 'last_name', 'email')