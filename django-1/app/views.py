from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

from .forms.customer_signup_form import CustomerSignupForm




# Create your views here.

def home(request):
    
    bio_data = 'Django practice project'

    bio_data = [1,2,3,4,5,6,7,8,9,10]

    bio_data = {
        'name' : 'Ahmad' , 
        'age'  : 20 ,
        'education' : 'Matric',
        'location' : 'Lahore'
    }

    # return HttpResponse(bio_data)
    # return render(request,'home.html', { 'data': 'data' })
    return render(request,'home.html', { 'data': bio_data })

def shop(request):
    return render(request,'shop.html')
    # return HttpResponse('shop page.')

def cart(request):
    return HttpResponse('cart page.')

def product_details(request,id):
    return HttpResponse( f'product details id is :{id}' )


def signup_customer(request):
    if request.method == 'GET':
        return render(request,'signup_customer.html')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if first_name and email and phone and  password and  (password == confirm_password):

            customer = Customer( 
                first_name = first_name,
                last_name = last_name,
                email = email,
                phone = phone,
                password = password  
                )
            
            customer.save()


            return HttpResponse('user created successfully!!!')
        else:
            return HttpResponse('provide valid info!!!')
        
        return HttpResponse(first_name )

def customers(request):
    customers = Customer.objects.all()
    return render(request,'customers.html',{'customers' : customers} )

    # return HttpResponse(customers)

    # customers = Customer.objects.get( )
    # customers = Customer.objects.filter( )

def update_customer(request,id):

    customer = Customer.objects.get( id = id )
    if request.method == 'GET':    
        # return HttpResponse( customer.first_name )


        return render(request,'update_customer.html', { 'customer' : customer } )
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        if first_name and email and phone:
            
            customer.first_name = first_name
            customer.last_name = last_name
            customer.email = email
            customer.phone = phone
            customer.save()
            return HttpResponse('user record updated successfully!!.')

        else:
            return HttpResponse('provide valid info!!!')

        return HttpResponse( request.POST )
    

def delete_customer(request, id):
    customer = Customer.objects.get( id = id)
    customer.delete()

    return HttpResponse( f'{id} is deleted ' )

# def signup_customer_form(request):
#     if request.method == 'GET':
#         form = CustomerSignupForm()
#         return render(request, 'signup_customer_form.html', { 'form' : form })
#     else:
#         form = CustomerSignupForm( request.POST )

#         if form.is_valid():

#             first_name = request.POST['first_name']
#             last_name = request.POST['last_name']
#             email = request.POST['email']
#             phone = request.POST['phone']
#             password = request.POST['password']
#             confirm_password = request.POST['confirm_password']

#             if password == confirm_password :
#                 customer = Customer( 
#                     first_name = first_name,
#                     last_name = last_name,
#                     email = email,
#                     phone = phone,
#                     password = password  
#                     )
                
#                 customer.save()

#             return HttpResponse( 'saving in db' )
#         else:
#             return HttpResponse('in valid info')
        

def signup_customer_model_form(request):
    if request.method == 'GET':
        form = CustomerSignupForm()
        return render(request, 'signup_customer_form.html', { 'form' : form })
    else:
        form = CustomerSignupForm( request.POST )

        if form.is_valid():
            form.save()
           
            return HttpResponse( 'saving in db' )
        else:
            return HttpResponse('in valid info')
