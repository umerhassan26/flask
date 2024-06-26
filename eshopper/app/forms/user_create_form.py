from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class UserCreateForm(UserCreationForm):

    class Meta:
        # fields = ('__all__')
        fields = ('first_name','last_name','username','password1','password2')
        model = User

    def __init__(self,*args, **kwargs):
        super(UserCreateForm,self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'Email / Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Conform Password'
