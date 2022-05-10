from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render (request, "index.html",context)

def contact(request):
    context = {}
    return render(request, "contact.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)


def shop(request):
    context = {}
    return render (request, "shop.html",context)

def sign_in(request):
    context = {}
    return render(request, "sign_in.html", context)

def sign_up(request):
    context = {}
    return render(request, "sign_up.html", context)