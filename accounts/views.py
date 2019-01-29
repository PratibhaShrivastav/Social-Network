from django.shortcuts import render
from django.views.generic import TemplateView,CreateView, DetailView
from accounts.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
# Create your views here.


class HomePage(TemplateView):
    template_name='index.html'


class SignUp(CreateView):
    form_class=CreateUserForm
    success_url=reverse_lazy('login')
    template_name='accounts/signup.html'

class CreateProfile(LoginRequiredMixin,CreateView):
    model = Profile
    fields = ('contact','gender','profile_pic')
    template_name = 'Profile/profile_form.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        username = self.kwargs.get('username')
        pk = self.object.pk
        return reverse_lazy('accounts:profile', kwargs={'username':username,'pk':pk})

class DetailProfile(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'Profile/profile_detail.html'
    context_object_name = 'profile'