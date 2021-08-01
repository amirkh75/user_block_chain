from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from actions.utils import create_action
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django import http
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = True
            user.save()
            create_action(user, 'signup', user)
            return HttpResponseRedirect(reverse_lazy('login'))
        return HttpResponseRedirect(reverse_lazy('signup'))


class LoginView(View):
    form_class = CustomUserAuthenticationForm
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                create_action(user, 'login', user)
                return HttpResponseRedirect(reverse_lazy('home'))
            else:
                return HttpResponse("be active!!!!!!")
        else:
            return HttpResponseRedirect(reverse_lazy('home'))

        return render(request, "registration/login.html")

    def get(self, request):
        form = self.form_class()
        return render(request, "registration/login.html", {'form': form})

class LogoutView(View):
    def get(self, request):
        user = request.user
        create_action(user, 'logout', user)
        logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))