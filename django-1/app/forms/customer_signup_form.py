from django import forms
from ..models import Customer


# class CustomerSignupForm( forms.Form  ):
class CustomerSignupForm( forms.ModelForm  ):
    first_name = forms.CharField( max_length=100 , widget= forms.TextInput( attrs= {'placeholder' : 'First Name' }))
    last_name = forms.CharField( max_length=100 , required=False)
    email = forms.EmailField( widget= forms.TextInput( attrs= { 'class' : 'form-control' } ) )
    phone = forms.CharField(max_length=11  )
    password = forms.CharField( widget= forms.PasswordInput() )
    confirm_password = forms.CharField( widget= forms.PasswordInput() )
    

    class Meta:
        # fields = ('__all__')
        fields = ('first_name','last_name','email','phone','password')
        model = Customer

