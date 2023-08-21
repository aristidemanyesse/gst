from django.shortcuts import render
from annoying.decorators import render_to

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