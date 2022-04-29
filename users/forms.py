from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.core.exceptions import ValidationError

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(label=("Email"),max_length=254, required=True)
    class Meta:
        model=CustomUserModel
        fields = ('username', 
        'first_name', 
        'last_name', 
        'email', 
        'profile_picture', 
        'password1', 
        'password2')
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUserModel.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('User with that email already exists')
        return email



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')



#password reset qilyotganda jonatgan email bazada bor yoki yo'q ekanligini tekshirish
class PasswordResetFormOverride(PasswordResetForm):
    class Meta:
        model = CustomUserModel
        fields = ('email')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if not CustomUserModel.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError('"There is no user registered with the specified email address!"')
        return email
    