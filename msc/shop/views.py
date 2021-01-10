from django.shortcuts import render
from .models import product
from math import ceil

# Create your views here.
from django.http import HttpResponse


def index(request):
    products = product.objects.all()
    params={'allProds' : products }

    return render(request,"shop/index.html", params)


def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


def about(request):
    return HttpResponse("This shop is medical store for all allopathic and ayurvedic medicine")


