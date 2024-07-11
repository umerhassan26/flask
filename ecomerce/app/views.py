from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Brand, Category 

from django.db.models import Q



# Create your views here.
def home(request):
    # MOdal_name.objects.all()

    try:
        # 1- Fetch recoed, (Read)
        products = Product.objects.all()
        # products = Product.objects.get(id = 4 )
        # products = Product.objects.get(pk = 4 )
        # products = Product.objects.get(name = 'Frok' )
        # products = Product.objects.get(name = 'Frok', price =5000 )

        # products = Product.objects.filter(name = 'Frok', price = 1000 )
        # products = Product.objects.filter( Q( name = "Froks") | Q(price = 1000 )  )


        # return HttpResponse(products.count())

        # 2 - create new record 
        # category = Category( name = 'Mens' )
        # category.save()

        # category = Category.objects.get(pk = 2)
        # brand = Brand.objects.get(pk = 1)


        # product = Product( name = 'Pent', price = 3000, qty = 200, availability = True, condition = True,  category = category, brand = brand )
        # product.save()

        # 3 -  update

        # category = Category.objects.get(pk =3 )
        # category.name = 'Womens'
        # category.save()

        # product = Product.objects.get(pk = 4)
        # product.name = "Easy Polo Gray Edition"
        # product.price = 5000
        # product.qty = 200
        # product.condition = False
        # product.category = category
        # product.brand = brand
        # product.save()


        # 4 -  delete

        # brand = Brand.objects.get(id = 4)
        # brand.delete()

        # return HttpResponse(brand)










    except:
        return HttpResponse('INvalid credentials')



    # return HttpResponse(products)
    return render(request,'home.html', {'products':products  })
    # return HttpResponse(products)
    # return HttpResponse('Hello HOme!')