from django.shortcuts import render
from django.http import HttpResponse    
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contect(request):
    return render(request,'contect.html')

def skills(request):
    return render(request,'skills.html')

def project(request):
    return render(request,'project.html')

def certificate(request):
    return render(request,'certificate.html')
