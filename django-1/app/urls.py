from django.urls import path

# from .views import home, index
from . import views

urlpatterns = [
    path('',views.home ),
    path('shop/',views.shop ),
    path('cart/',views.cart ),
    # path('product-details/',views.product_details ),
    # path('product/details/',views.product_details ),
    # path('product/details/<id>/',views.product_details ),
    path('product/details/<int:id>/',views.product_details , name= 'product_details' ),
    path('register/', views.signup_customer , name='signup_customer'),
    path('customers/', views.customers , name='customers'),
    path('customer/edit/<int:id>', views.update_customer , name='update_customer'),
    path('customer/delete/<int:id>', views.delete_customer , name='delete_customer'),
]