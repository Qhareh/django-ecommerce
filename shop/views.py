from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

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

def submitContactForm(request):

    if request.method == "POST":
    ## handle form data
      form_data =request.POST
      email = form_data["email"]
      name = form_data["name"]
      phone = form_data["phone"]
      message = form_data["message"]
 
      return HttpResponseRedirect("/form/success")
    
    else:
        return HttpResponseRedirect("/")
     
def successRedirect(request):
    context = {
     
    }

    return render(request, "success.html", context)    

def ajaxContactSubmission(request):
   
    email = request.POST["email"]
    name = request.POST["name"]
    number = request.POST["phone"]
    message = request.POST["message"]

    context = {
        "success": True,
        "message": "Thank you "+name+" for your message"
    }

    return JsonResponse(context)