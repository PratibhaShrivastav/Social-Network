from django.contrib import admin
from groups.models import Group,Groupmember
# Register your models here.


class GroupmemberInline(admin.TabularInline):
    model = Groupmember
)

admin.site.register(Group)