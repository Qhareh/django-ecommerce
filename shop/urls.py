from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name="home"),
    path('contact',contact, name="contact"),
    path('about',about, name="about"),
    path('shop',shop, name="shop"),
    path('sign_in',sign_in, name="sign_in"),
    path('sign_up',sign_up, name="sign_up"),
    path('contact/form/submit', submitContactForm, name="contact.form"),
    path('form/success', successRedirect, name="success.redirect"),
    path("ajax/contact/submission", ajaxContactSubmission, name="contact.ajax.submission")
  ]

