from django.shortcuts import render

def landing(request):
    return render(request, 'landing/landing.html')

def login(request): 
    return render(request, 'login/login.html')
def signup(request):
    return render(request,  'login/signup.html')