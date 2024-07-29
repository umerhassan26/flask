from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms.user_create_form import UserCreateForm
from .forms.checkout_form import CheckoutForm


from .models import Category, Brand, Product, Cart





# Create your views here.
def home(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'home.html')

def map(request):
    # return HttpResponse(request.user.is_authenticated)
    return render(request,'map.html')

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
    categories = Category.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.all()

    # return HttpResponse(brands)

    return render(request,'shop.html', {'categories':categories, 'brands' : brands , 'products' : products})

def product_details(request,id):
    product = Product.objects.get(id=id)
    # return HttpResponse(product)

    return render(request,'product_details.html' , {'product':product})

def checkout(request):

    total = 0
    user_id = request.user.id
    shipping_charges = 20.00
    cart_items = Cart.objects.filter(user = user_id)
    for item in cart_items:
        total = total + item.sub_total
    
    tax = float(total) * 0.17
    # return HttpResponse( tax )
    
    grand_total = float(total) + tax + shipping_charges
    # return HttpResponse(user_id)


    if request.method == 'GET':
        checkout_form = CheckoutForm()
        # return HttpResponse(checkout_form)

        return render(request,'checkout.html',{ 
        'cart_items': cart_items, 
        'total' :total, 
        'shipping_charges' : shipping_charges,
        'tax' : tax,
        'grand_total' :grand_total,
        'form' : checkout_form  })
    else:
        # return HttpResponse( request.user.email )
        form = CheckoutForm( request.POST )
        if form.is_valid():
            form.user = request.user
            form.order_price = grand_total
            form.save()
            # return HttpResponse(form.user)
        else:   
            return HttpResponse('invalid data.')
        return HttpResponse(request.POST)





def cart(request):
    total = 0
    user_id = request.user.id
    shipping_charges = 20.00
    cart_items = Cart.objects.filter(user = user_id)
    for item in cart_items:
        total = total + item.sub_total
    
    tax = float(total) * 0.17
    # return HttpResponse( tax )
    
    grand_total = float(total) + tax + shipping_charges
    # return HttpResponse(user_id)

    return render(request,'cart.html', { 
        'cart_items': cart_items, 
        'total' :total, 
        'shipping_charges' : shipping_charges,
        'tax' : tax,
        'grand_total' :grand_total } )

def add_to_cart(request):
    product_id = request.POST['product_id']
    qty = request.POST['quantity']
    
    product = Product.objects.get(pk=product_id)
    user_id = request.user.id
    
            # return HttpResponse(sub_total)

    try:
        # return HttpResponse(user_id)
        cart_item = Cart.objects.get(product = product, user = user_id)
        
    except:
        cart_item = None



    if cart_item is None:
        
        # create new entry in cart  
        sub_total = product.price * int(qty)
        cart = Cart(product=product, qty=qty, sub_total = sub_total, user = user_id)
        cart.save()
    else:
        # update the existing item qty
        cart_item.qty = cart_item.qty + int(qty)
        cart_item.sub_total =  cart_item.qty * product.price
        cart_item.save()


    # return HttpResponse(check_cart)
    
    

    return redirect('cart')
    # return HttpResponse(request)



def blogs(request):
    return render(request,'blogs.html')

def blog(request,id):
    return render(request,'blog.html')

def error_page(request):
    return render(request,'error_page.html')

def contact(request):
    return render(request,'contact.html')