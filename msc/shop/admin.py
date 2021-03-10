from django.contrib import admin

# Register your models here.
from .models import product
from .models import About
from .models import Customer
admin.site.register(product)
admin.site.register(About)
admin.site.register(Customer)