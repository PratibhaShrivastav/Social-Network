from django.contrib import admin
from groups.models import Group,Groupmember
# Register your models here.


admin.site.register(Group)

class GroupmemberInline(admin.TabularInline):
    model = Groupmember
