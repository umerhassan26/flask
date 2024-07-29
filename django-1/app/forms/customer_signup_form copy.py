from django import forms



class CustomerSignupForm( forms.Form ):
    first_name = forms.CharField( max_length=100 )
    last_name = forms.CharField( max_length=100 , required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11  )

    password = forms.CharField( widget= forms.PasswordInput() )
    confirm_password = forms.CharField( widget= forms.PasswordInput() )

    
