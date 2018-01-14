from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from user_sessions.forms import LoginForm, UserRegistrationForm


class LoginView(View):
    form_class = LoginForm
    template_name = 'user_sessions/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=un, password=pw)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('contacts:contact_list'))
            else:
                return render(request, self.template_name, {'form': form, 'error_message':
                    "Invalid Username or Password. Please try again. "})
        else:
            return render(request, self.template_name, {'form': form})


class HomePageView(View):
    template_name = 'phone_directory/home.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user_sessions:home'))


class AddUserView(View):

    form_class = UserRegistrationForm
    template_name = 'user_sessions/register_user.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('contacts:contact_list'))
        else:
            return render(request, self.template_name, {'form': form})
