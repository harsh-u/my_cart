from django.shortcuts import render
from .models import product, About, ShoppingCart, Catogery
from django.shortcuts import redirect


# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required



# Create your views here.
from django.http import HttpResponse

# @login_required
def index(request):
    products = product.objects.all()
    params={'allProds' : products}
    return render(request,"shop/index.html", params)

def signup(request):
    if request.method=="GET":
        return render(request,"shop/signup.html")
    else:
        return HttpResponse(request.POST.get('first_name'))
def login(request):
    return render(request,"shop/login.html")


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
    about = About.objects.all()[1]
    params = {'data':about }
    return render(request,"shop/about.html", params)


def test(request):
    return render(request,"shop/test.html")

def do_add_to_cart(product_id, number):
    prod = product.objects.get(pk=product_id)
    cart, _ = ShoppingCart.objects.get_or_create(product=prod)
    cart.count = cart.count + number
    cart.save()


def add_to_cart(request, product_id, number):
    do_add_to_cart(product_id, number)

    response = redirect('/shop/cart/')
    return response


def buy_now(request, product_id):
    do_add_to_cart(product_id, 1)

    response = redirect('/shop/cart/')
    return response

def remove(request,product_id):
    prod = product.objects.get(pk=product_id)
    prod.delete()
    response = redirect('/shop/cart/')
    return response





def cart(request):
    cart =  ShoppingCart.objects.all()
    params={'cart' : cart }
    return render(request,"shop/cart.html", params)


class NegativeIntConverter:
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value

