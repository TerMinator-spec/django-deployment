from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"app/index.html")

def other(request):
    return render(request,"app/other.html")

def relative(request):
    return render(request,"app/relative_url.html")
