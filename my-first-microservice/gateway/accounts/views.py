from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from core.clients import user_manager
from django.contrib import messages


class Register(View):
    form_class = RegisterForm
    template_name = 'authentication/register-page.html'

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            response = user_manager.create_user(form.cleaned_data)
            if 'error' in response.keys():
                messages.error(request,response['error'],'danger')
                return render(request,self.template_name,{'form':form})
            messages.success(request,'You Are Successfully Registered!','info')
            return redirect('accounts:login')
        return render(request,self.template_name,{'form':form})
        

class LoginPage(View):
    template_name = 'authentication/login-page.html'
    form_class = LoginForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            token = user_manager.get_token(form.cleaned_data)
            if token != 'error':
                request.session['access'] = token['access']
                request.session['refresh'] = token['refresh']
                messages.success(request,'You Successfully Logged in','success')
                return redirect('core:home')
            messages.error(request,'Email Or Password is Wrong!','danger')
        return render(request,self.template_name,{'form':form})


class Logout(View):
    
    def get(self,request):
        request.session['access'] = None
        request.session['refresh'] = None
        messages.success(request,'You Successfully Logged Out','info')
        return redirect('accounts:login')