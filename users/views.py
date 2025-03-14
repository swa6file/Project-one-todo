from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordContextMixin, PasswordChangeView, PasswordChangeDoneView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserChangePasswordForm


# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html '
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')



class ProfileUser(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title':"Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile',args=[self.request.user.pk])



class UserPasswordChange(PasswordChangeView):
    form_class = UserChangePasswordForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"

class UserPasswordChangeDone(PasswordChangeDoneView):
    template_name = "users/password_change_done.html"

