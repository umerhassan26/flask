from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.nameCl


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    qty = models.IntegerField()
    availability = models.BooleanField(default=1)
    condition = models.BooleanField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=0)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE) # delete the associate items on deleting the foreignkey value
    image = models.ImageField(upload_to='products/', default = '')


    def __str__(self):
        return f" {self.id} - {self.name} "  
    
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10,decimal_places=2)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.qty} - {self.sub_total}"
