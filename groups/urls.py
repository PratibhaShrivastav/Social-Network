from django.urls import path,re_path
from groups.views import Creategroup,Singlegroup,Listgroup,JoinGroup,LeaveGroup

app_name='groups'

urlpatterns = [
    path('new/',Creategroup.as_view(),name="create"),
    path('',Listgroup.as_view(),name="all"),
    re_path('posts/in/(?P<slug>[-\w]+)/',Singlegroup.as_view(),name="single"),
    re_path('join/(?P<slug>[-\w]+)/',JoinGroup.as_view(),name="join"),
    re_path('leave/(?P<slug>[-\w]+)/',LeaveGroup.as_view(),name="leave"),
]
