from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from groups.models import Group
# Create your views here.


class Creategroup(CreateView):
    model= Group
    fields=('name','description')

class Singlegroup(DetailView):
    model=Group

class Listgroup(ListView):
    model=Group