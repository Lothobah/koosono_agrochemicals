from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from agrochemicals_management_system.EmailBackEnd import EmailBackEnd
from django.urls import reverse
from django.contrib.auth import views as auth_views
# Create your views here.
def home(request):
    return render(request, "login_page.html")


def DoLogin(request):
    try:
        if request.method != "POST":
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")
            #return HttpResponse("<h3>This account was deleted<h3/>")
        else:
            user = EmailBackEnd.authenticate(request, username=request.POST.get(
                "username"), password=request.POST.get("password"))  # email
            if user != None:
                login(request, user)
                if user.user_type == "1":
                    return HttpResponseRedirect("/products")
                #elif user.user_type == "2": 
                    #return HttpResponseRedirect(reverse("staff_homepage"))
                #else:
                    #return HttpResponseRedirect(reverse("student_homepage"))
            else:
                messages.error(
                    request, 'Your Username or Password is incorrect.')
                return HttpResponseRedirect("/")
    except:
        return HttpResponseRedirect("/")
def Logout_User(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return HttpResponseRedirect("/")
