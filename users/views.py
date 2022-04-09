from django.shortcuts import redirect, render
from django.views import View
from .forms import UserCreationForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login


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
            return redirect('/')
        else:
            return render(request, 'users/login.html', context)
    