from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import CustomUser, Follows
from articles.models import Article
from upload_validator import FileTypeValidator


def dashboard(request, user_id):
    # Get visited page's user id to show his/her properties

    guest_user = CustomUser.objects.get(id=user_id)

    # Get articles
    articles = Article.objects.filter(writer=guest_user)

    # Get followers and followed users from model's static method
    followers = Follows.get_followers(guest_user)
    followed = Follows.get_followed(guest_user)
    if guest_user.email in followers:
        print("okey")

    context = {

        'user_guest': guest_user,
        'articles': articles,
        'followers': followers,
        'followed': followed,
    }

    return render(request, 'accounts/dashboard.html', context)


def login(request):
    if request.method == 'POST':

        # Get form values
        password = request.POST['password']
        username = request.POST['username']

        user = auth.authenticate(username=username, password=password,)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, ' You are now logged in')
            return redirect('pages:index')
        else:
            # messages.error(request, 'Invalid credentials')
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
            # Check username
            User = get_user_model()
            if User.objects.filter(username=username).exists():
                # messages.error(request,'This username is taken')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    # messages.error(request,'This email is being used')
                    return redirect('accounts:register')

                else:

                    # looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email)
                    # login after register
                    # auth.login(request,user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    # messages.success(request, ' You are now registered')
                    return redirect('accounts:login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return redirect('accounts:login')

    return redirect('accounts:login')


def change_profile_settings(request):
    # form yapılacak
    if request.method == 'POST':
        # Access our user - This maybe different
        user_id = request.user.id
        user = CustomUser.objects.get(id=user_id)

        # Get all post variables
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birth_date = request.POST['birth_date']
        blogname = request.POST['blogname']
        description = request.POST['description']
        about = request.POST['about']
        if 'image' in request.FILES:
            image = request.FILES['image']

            validator = FileTypeValidator(
                allowed_types=['image/jpeg',"image/png","image/jpg"],
                allowed_extensions=['.jpg', '.png']
            )

            try:
                validator(image)
            except:
                user_id = request.user.id
                return redirect('accounts:dashboard',user_id)
            user.photo = image

        # Update user attiributes
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        #user.birth_date = birth_date
        user.blogname = blogname
        user.description = description
        user.about = about

        user.save()

        return redirect('accounts:dashboard', user_id)

    else:
        return redirect('accounts:dashboard')


def follow(request):
    if request.method == 'POST':
        user = request.user

        follow_id = request.POST['user_id']
        followed_user = CustomUser.objects.get(pk=follow_id)
        if not Follows.objects.filter(follower=user, followed=followed_user).exists() and follow_id != followed_user:
            follow = Follows(follower=user, followed=followed_user)
            follow.save()
    return redirect('accounts:dashboard',followed_user.id)



def unfollow(request):
    if request.method == 'POST':
        user = request.user

        unfollow_id = request.POST['user_id']
        unfollowed_user = CustomUser.objects.get(pk=unfollow_id)
        Follows.objects.get(follower=user,followed=unfollowed_user).delete()

    return redirect('accounts:dashboard',unfollowed_user.id)
