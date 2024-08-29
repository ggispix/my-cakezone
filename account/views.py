from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


# Create your views here.
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(self.success_url)


class MyLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return self.request.GET.get('next', '/')


def user_logout(request):
    logout(request)
    return redirect('home:index')