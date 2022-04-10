from django.shortcuts import redirect, render
from django.views import View
from .forms import UserCreationForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.
class RegisterView(View):
    def get(self, request):
        create_form = UserCreationForm
        context={
            'form':create_form
        }
        return render(request, 'users/register.html', context=context)

    
    def post(self, request):
        create_form=UserCreationForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect("users:login")
        else:
            context={
            'form':create_form
            }
            return render(request, 'users/register.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'form':login_form
        }

        return render(request, 'users/login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        context = {
            'form':login_form
        }
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user) #sessiya ochib, sessiya id sini cookie ga yozib qoyadi
            messages.success(request, 'Successfully logged in.')
            return redirect('/')
        else:
            return render(request, 'users/login.html', context)

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)  #yuqorida logout ni chaqirib olganmiz
        messages.info(request, "Successfully logged out")
        return redirect('/')    

class ProfileView( LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'user':request.user
        }
    
        return render(request, 'users/profile.html', context)

