from django.shortcuts import render
from .models import product, About, ShoppingCart, Category, Customer
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import AddressForm
from django.http import HttpResponseRedirect

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
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        user, created = User.objects.get_or_create(username=email)
        if created:
            user.email = email
            user.password = password
            user.first_name= first_name
            user.last_name = last_name
            user.save()

            customer, _ = Customer.objects.get_or_create(user=user)
            customer.phone = mobile
            customer.save()

        return HttpResponse(f"{first_name} {last_name}")

def login(request):
    return render(request,"shop/login.html")

def address(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/shop/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddressForm()

    return render(request, 'shop/address.html', {'form': form})


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

