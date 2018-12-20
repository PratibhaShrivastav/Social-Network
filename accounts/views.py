from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from accounts.forms import CreateUserForm
from django.urls import reverse_lazy

# Create your views here.

class HomePage(TemplateView):
    template_name='index.html'


class SignUp(CreateView):
    form_class=CreateUserForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'
