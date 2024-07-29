from django import forms
from ..models import Order


class CheckoutForm(forms.ModelForm):
    title = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'Title' } ) )
    first_name = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'First Name' } ) )
    middle_name = forms.CharField(required=False , widget= forms.TextInput( attrs={'placeholder' : 'Middle Name' } ) )
    last_name = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'last Name' } ) )
    email = forms.EmailField( widget= forms.TextInput( attrs={'placeholder' : 'Email' } ) )
    phone = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : 'Phone' } ) )
    address1 = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Enter address' } ) )
    address2 = forms.CharField(required=False, widget= forms.TextInput( attrs={'placeholder' : ' Enter address (more) ' } ) )
    zip_code = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Zip / Postal Code ' } ) )
    city = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' City ' } ) )
    state = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' State ' } ) )
    country = forms.CharField( widget= forms.TextInput( attrs={'placeholder' : ' Country ' } ) )
    note = forms.Textarea()
    user = forms.CharField(required=False)

    class Meta:

        fields = ('__all__')
        model = Order


       





