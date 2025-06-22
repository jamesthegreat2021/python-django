from django.http import HttpResponse
#ths allows to render the html template to the browser, render is the function or method 
from django.shortcuts import render

def homepage(request): 
    
    #return HttpResponse("hello you are at the homepage")
    return render(request, 'homepage.html')

def about(request): 

    #return HttpResponse("this is me, james the programmer")
    return render(request, 'about.html')