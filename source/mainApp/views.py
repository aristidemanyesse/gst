from django.shortcuts import redirect, render
from annoying.decorators import render_to
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from mainApp.models import Employe
# Create your views here.


@render_to('mainApp/index.html')
def main(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('mainApp/services.html')
def services(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('mainApp/contacts.html')
def contacts(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('mainApp/login.html')
def login_(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
    
@render_to('mainApp/login.html')
def connexion(request):
    if request.method == "POST":
        erreur = ""
        
        datas = request.POST
        user = authenticate(request, username=datas["username"], password=datas["password"])
        if user is None:
            erreur = "Username ou mot de passe incorrect !"
        else:
            login(request, user)
            return redirect('mainApp:liste')
     
        ctx = {
            "erreur": erreur
        }
        return ctx
    
    
@render_to('mainApp/liste.html')
def liste(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect('login')

        employes = Employe.objects.filter(deleted = False)
        ctx = {
            "employes": employes
        }
        return ctx
    
    
@render_to('mainApp/user.html')
def user(request, code):
    if request.method == "GET":
        employe = Employe.objects.filter(deleted = False, code = code).first()
        if employe is not None:
            ctx = {
                "employe": employe
            }
            return ctx

        else:
            return redirect("mainApp:main")