from django.contrib import admin
from .models import Category, Brand, Product, Cart

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','qty','availability','condition','category','brand')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product','qty','sub_total' , 'user')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart,CartAdmin)
admin.site.register(Product,ProductAdmin)
