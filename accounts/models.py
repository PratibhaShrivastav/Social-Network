from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

class Profile(models.Model):
    
    GENDER_OPTIONS = (
        ('ML','MALE'),
        ('FM','FEMALE'),
        ('OT','OTHER'),
    )
    user = models.ForeignKey(auth.models.User,related_name='profile',on_delete=models.CASCADE,null=True,blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_OPTIONS)
    contact = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images/',default='images/default.png',null=True,blank=True)

    def __str__(self):
       return self.user.username

class ContactUs(models.Model):

    email = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.title