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
    path('product/details/<int:id>/',views.product_details ),
]