from django.urls import path,re_path
from accounts.views import SignUp,CreateProfile,DetailProfile,VerifyProfile,ContactUs, send_request
from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns=[
    path('signup/',SignUp.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('<slug:username>/profile/create', CreateProfile.as_view(), name='createprofile'),
    path('<slug:username>/profile/<int:pk>/', DetailProfile.as_view(), name='profile'),
    path('<slug:username>/profile/',VerifyProfile , name='verifyprofile'),
    path('',ContactUs.as_view(), name='contactus'),
    path('add_friend/<int:to_user>/', send_request, name='send_request'),
]