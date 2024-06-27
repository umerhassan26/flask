from django.contrib import admin
from .models import Category, Brand, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','qty','availability','condition','category','brand')


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product,ProductAdmin)
