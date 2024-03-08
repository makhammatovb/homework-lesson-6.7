from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the page</h1>")

def about(request):
    return HttpResponse("<h1>Hello, world. You're at the about page</h1>")

def contact(request):
    return HttpResponse("<h1><a href=\"mailto:<EMAIL>\">Contact</a></h1>")

def services(request):
    return HttpResponse("<h1>This page contains our services </h1>")

def staff(request):
    return HttpResponse("<h1>This page is about our staff </h1>")