from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import CustomUser
from articles.models import Article


# Create your views here.

def dashboard(request):

    user_id                 = request.user.id
    user                    = CustomUser.objects.get(id=user_id)

    followers               = user.follower
    followed                = user.followed
    articles                = user.articles
    liked_articles          = user.liked_articles
    disliked_articles       = user.disliked_articles
    followers_list          = []
    followed_list           = []
    articles_list           = {}
    liked_articles_list     = {}
    disliked_articles_list  = {}

    for id in followers:
        followers_list.append(CustomUser.objects.get(id=id).username)

    for id in followed:
        followed_list.append(CustomUser.objects.get(id=id).username)

    for id in articles:
        articles_list.update({Article.objects.get(id=id).id:Article.objects.get(id=id).title})

    for id in articles:
        articles_list.update({Article.objects.get(id=id).id:Article.objects.get(id=id).title})

    for id in liked_articles:
        liked_articles_list.update({Article.objects.get(id=id).id:Article.objects.get(id=id).title})

    for id in disliked_articles:
        disliked_articles_list.update({Article.objects.get(id=id).id:Article.objects.get(id=id).title})
    


    context = {

        'user':user,
        'follower_list':followers_list,
        'articles_list':articles_list,
        'liked_articles':liked_articles_list,
        'disliked_articles':disliked_articles_list,
    }

    return render(request, 'accounts/dashboard.html',context)

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
        username    = request.POST['username']
        email       = request.POST['email']
        password    = request.POST['password']
        password2   = request.POST['password2']


        # Check if password match
        if password == password2:
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

def change_profile_settings(request):
    if request.method == 'POST':
        
        # Get all post variables
        email       = request.POST['email']
        first_name  = request.POST['first_name']
        last_name   = request.POST['last_name']
        birth_date  = request.POST['birth_date']
        blogname    = request.POST['blogname']
        description = request.POST['description']

        
        # Access our user - This maybe different
        user_id = request.user.id
        user = CustomUser.objects.get(id=user_id)

        # Update user attiributes
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.birth_date = birth_date
        user.blogname = blogname
        user.description = description
        user.save()

        return redirect('accounts:dashboard')


    else:
        return redirect('accounts:dashboard')