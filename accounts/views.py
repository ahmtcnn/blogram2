from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import CustomUser
from articles.models import Article


# Create your views here.

def dashboard(request, user_id):

    user_id                 = user_id
    guest_user                    = CustomUser.objects.get(id=user_id)

    followers_list          = guest_user.follower
    followed_list           = guest_user.followed
    articles_list           = guest_user.articles
    liked_articles_list     = guest_user.liked_articles
    disliked_articles_list  = guest_user.disliked_articles
    followers               = []
    followed                = []
    articles                = []
    liked_articles          = []
    disliked_articles       = []

    for id in followers_list:
        followers.append(CustomUser.objects.get(id=id))

    for id in followed_list:
        followed.append(CustomUser.objects.get(id=id))

    for id in articles_list:
        try:
            articles.append(Article.objects.get(id=id))
        except:
            articles = []

    for id in liked_articles_list:
        liked_articles.append(Article.objects.get(id=id))

    for id in disliked_articles:
        disliked_articles.append(Article.objects.get(id=id))
    


    context = {

        'user_guest':guest_user,
        'followers':followers,
        'followed':followed,
        'articles':articles,
        'liked_articles':liked_articles,
        'disliked_articles':disliked_articles,
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
            return redirect('pages:index')
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

def follow(request):
    if request.method == 'POST':
        user = request.user

        follow_id = request.POST['user_id']

        user.followed.append(follow_id)
        #print(follow_id)

    return render(request, 'accounts/dashboard.html')




def unfollow(request):
    if request.method == 'POST':
        user = request.user

        follow_id = request.POST['user_id']

        user.followed.remove(follow_id)    

    return render(request, 'accounts/dashboard.html')
