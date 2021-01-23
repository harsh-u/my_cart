from django.urls import path
from django.urls import register_converter
from shop import views
register_converter(views.NegativeIntConverter, 'negint')

from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="ContactUs"),
    path("productview/", views.productview, name="ProductView"),
    path("tracker/", views.tracker, name="TrackStatus"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("test/", views.test, name="test"),
    path("add_to_cart/<int:product_id>/<negint:number>", views.add_to_cart, name="add_to_cart"),
    path("buy_now/<int:product_id>", views.buy_now, name="buy_now"),
    path("cart/", views.cart, name="cart"),
]

app_name = 'shop'