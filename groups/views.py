from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from groups.models import Group
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404
from groups.models import Group,Groupmember
from django.contrib import messages
from django.db import IntegrityError
from . import models
# Create your views here.


class Creategroup(CreateView):
    model=Group
    fields=('name','description')
    success_url=reverse_lazy('groups:all')

class Singlegroup(DetailView):
    model=Group

class Listgroup(ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug' : self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group=get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            Groupmember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,"Warning! You are not a user!")
        else:
            messages.success(self.request,"You are now a member!")
        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug' : self.kwargs.get('slug')})
    
    def get(self, request, *args, **kwargs):

        try:
            membership=models.Groupmember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except models.Groupmember.DoesNotExist:
            messages.warning(self.request,"Sorry you are not in this group!")
        else:
            membership.delete()
            messages.success(self.request,"You have left the group")



        return super().get(request, *args, **kwargs)

