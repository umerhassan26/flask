from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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