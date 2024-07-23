from django.shortcuts import render
from django.http import HttpResponse


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

