from django.contrib import admin

# Register your models here.
from .models import product
from .models import About
admin.site.register(product)
admin.site.register(About)