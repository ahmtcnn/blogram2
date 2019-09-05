from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout(request):
    return redirect('index')