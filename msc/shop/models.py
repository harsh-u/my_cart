from django.db import models
from django import forms

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    catogery = models.CharField(max_length=50, default="")
    subcatogery = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class ShoppingCart(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

class About(models.Model):
    about = models.TextField()
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    pin_code = models.CharField(max_length=6, blank=True)
    email_id = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.name
class Customer(models.Model):
    first_name=forms.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)