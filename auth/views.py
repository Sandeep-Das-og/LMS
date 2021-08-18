from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import View

from django.shortcuts import redirect, render
from auth import forms
from django.contrib.auth import login

class Login(LoginView):
    template_name = 'auth/login.html'

class Logout(LogoutView):
    pass

class SignUp(View):
    def get(self, request):
        context = {
            "form" : forms.RegistrationForm()
        }
        return render(request, 'auth/signup.html', context)


    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('/')
        
        context = {
            "form" : form
        }
        return render(request, 'auth/signup.html', context)

