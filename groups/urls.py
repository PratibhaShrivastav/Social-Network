from django.urls import path,re_path
from groups.views import Creategroup,Singlegroup,Listgroup

app_name='groups'

urlpatterns = [
    path('new/',Creategroup.as_view(),name="create"),
    path('',Listgroup.as_view(),name="all"),
    re_path('posts/in/(?P<slug>[-\w]+)/',Singlegroup.as_view(),name="single"),
]
