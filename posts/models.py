from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from groups.models import Group
from django.utils import timezone
# Create your models here.
import misaka

User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts')
    message=models.TextField()
    message_html=models.TextField(editable=False)
    created_at=models.DateTimeField(default=timezone.now)
    group=models.ForeignKey(Group,related_name='posts',null=True,blank=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username,'pk':self.pk})

    class Meta:
        ordering =['-created_at']
        unique_together=['user','message']
    