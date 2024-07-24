from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer



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