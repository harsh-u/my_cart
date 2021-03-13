from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}-{self.sub_category}"

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, default=None)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
    phone=models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}({self.phone})"

class Address(models.Model):
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address1} {self.address2}"

