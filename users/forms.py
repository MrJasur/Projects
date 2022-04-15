from dataclasses import field
from pyexpat import model
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

#Biz LoginView da UserLOgin formdan foydalanamadik. Uning orniga AuthenticationForm dan foydalandik
#AuthenticationForm usrname va passwordni cleaned data qilib ham beradi
# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')