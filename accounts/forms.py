from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CreateUserForm(UserCreationForm):
    
    email=forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['style'] = "width:540px;"
        self.fields['email'].widget.attrs['style'] = "width:540px"
        self.fields['password1'].widget.attrs['style'] = "width:540px"
        self.fields['password2'].widget.attrs['style'] = "width:540px"

    class meta:
        fields=('username','email','password1','password2')
        model=get_user_model