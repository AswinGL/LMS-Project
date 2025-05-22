
from django.shortcuts import render

from django.views import View

from . forms import LoginForm

# Create your views here.

class LoginView(View):

    def get(self, request,*args, **kwargs):

        form = LoginForm()

        data = {'page':'login-page'}

        return render(request, 'authentication/login.html',context=data)
    
class LogoutView(View):

    def get(self, request,*args, **kwargs):

        data = {'page':'logout-page'}

        return render(request, 'authentication/logout.html',context=data)