from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, This is my first Django Project, you are at Home page. ")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, This is my first Django Project, you are at About page. ")
    return render(request,'website/about.html')

def contact(request):
    # return HttpResponse("Hello, This is my first Django Project, you are at Contact page. ")
    return render(request,'website/contact.html')

def career(request):
    return render(request,'website/career.html')