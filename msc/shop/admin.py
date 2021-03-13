from django.contrib import admin

# Register your models here.
from .models import product
from .models import About
from .models import Customer, Category, Address
admin.site.register(product)
admin.site.register(About)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Address)