from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout

from .forms.user_create_form import UserCreateForm



# Create your views here.
def home(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'home.html')

def user_login(request):
    if request.method == "GET":
        # form = UserCreationForm()
        
        form = UserCreateForm()
        # return HttpResponse(form)
        return render(request,'login.html',{'form':form} )
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password= password)

        if user is None:
            return HttpResponse('invalid credentials!!!')
        else:
            login(request,user)
            return HttpResponse('successfully logged in!!')




        return HttpResponse(request)

def user_logout(request):
    logout(request)
    return HttpResponse('User is Successfully logged out!!!')


def register(request):
    if request.method == 'POST':
        
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('user created successfully!')
        else:
            return HttpResponse('please provide authentic data')

        return HttpResponse(request)

    else:
        return HttpResponse('not allowed')


def shop(request):
    return render(request,'shop.html')

def product_details(request,id):
    return render(request,'product_details.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')

def blogs(request):
    return render(request,'blogs.html')

def blog(request,id):
    return render(request,'blog.html')

def error_page(request):
    return render(request,'error_page.html')

def contact(request):
    return render(request,'contact.html')