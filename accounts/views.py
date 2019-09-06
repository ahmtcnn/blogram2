from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login(request):
    if request.method == 'POST':
        
        # Get form values
        password = request.POST['password']
        username = request.POST['username']


        user = auth.authenticate(username=username, password=password,)

        if user is not None:
            auth.login(request, user)
            #messages.success(request, ' You are now logged in')
            return redirect('accounts:dashboard')
        else:
            #messages.error(request, 'Invalid credentials')
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        # Check if password match
        if password == password2:
            print("girdi1")
            #Check username
            User = get_user_model()
            if User.objects.filter(username = username).exists():
                #messages.error(request,'This username is taken')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email = email).exists():
                    #messages.error(request,'This email is being used')
                    return redirect('accounts:register')

                else:

                    #looks good
                    user = User.objects.create_user(username=username, password=password, email=email)
                    #login after register
                    #auth.login(request,user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')  
                    user.save()
                    #messages.success(request, ' You are now registered')
                    return redirect('accounts:login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        #messages.success(request, 'You are now logged out')
        return redirect('pages:index')

    return redirect('pages:index')