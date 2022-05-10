from django.urls import path
from .views import home,contact,about, shop, sign_in, sign_up
urlpatterns = [
    path('',home, name="home"),
    path('contact',contact, name="contact"),
    path('about',about, name="about"),
    path('shop',shop, name="shop"),
    path('sign_in',sign_in, name="sign_in"),
    path('sign_up',sign_up, name="sign_up"),
  ]