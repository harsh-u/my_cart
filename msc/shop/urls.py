from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About"),
    path("contact/", views.contact, name="ContactUs"),
    path("productview/", views.productview, name="ProductView"),
    path("tracker/", views.tracker, name="TrackStatus"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),

]
