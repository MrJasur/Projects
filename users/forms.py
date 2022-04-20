from django import forms
from .models import CustomUserModel

class UserCreationForm(forms.ModelForm):
    class Meta:
        model=CustomUserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'profile_picture')


    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')