from tempfile import template

from django.shortcuts import render

#
def home(request):
    return render(request, 'index.html')
def customdesigns(request):
    return render(request,'customdesigns.html')
def newdesigns(request):
    return render(request,'newdesigns.html')

def plainbaskets(request):
    return render(request,'plainbaskets.html')