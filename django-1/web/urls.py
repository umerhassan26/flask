from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.home),
    path('shop', views.shop),
    # path('product/details/<id>', views.product_details),
    path('product/details/<int:id>', views.product_details),
    # path('',)
]