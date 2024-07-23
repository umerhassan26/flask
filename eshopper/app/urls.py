from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('map/', views.map ,name='map'),
    path('login/', views.user_login ,name='login'),
    path('logout/', views.user_logout ,name='logout'),
    path('register/', views.register ,name='register'),
    path('shop/', views.shop ,name='shop'),
    path('checkout/', views.checkout ,name='checkout'),
    path('cart/', views.cart ,name='cart'),
    path('cart/add', views.add_to_cart ,name='add_to_cart'),
    path('blogs/', views.blogs ,name='blogs'),
    path('error/404/', views.error_page ,name='error_page'),
    path('contact', views.contact ,name='contact'),
    path('blog/<id>/', views.blog ,name='blog'),
    path('product/details/<id>/', views.product_details ,name='product_details'),

]