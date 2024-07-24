from django.contrib import admin
from .models import Customer

# from . import models
# admin.site.register( models.Customer )


class CustomerAdmin( admin.ModelAdmin ):
    list_display = ('id', 'first_name', 'last_name' ,'phone', 'email')


# Register your models here.
admin.site.register( Customer,CustomerAdmin )
