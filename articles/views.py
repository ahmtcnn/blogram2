from django.shortcuts import render, redirect
from .models import Article, Likes
from accounts.models import CustomUser
from django.http import JsonResponse
from .forms import ArticleForm

# Create your views here.


def index(request):
    # if request.user.is_authenticated:
    # We fetch the article objects to print them on index page
    articles = Article.objects.all()
    liked_articles = Likes.get_liked_articles(request.user)

    context = {
            'articles': articles,
            'liked_articles':liked_articles
        }

    return render(request, 'articles/articles.html', context,status=200)



def article(request, article_id):

    article = Article.objects.get(id=article_id)

    context = {

        'article': article,
    }

    return render(request, 'articles/article.html', context)


def search(request):
    return render(request, 'articles/search.html')


def save_article(request):
    # Check if request is post
    if request.method == 'POST':
        
        # Get user object
        user = request.user

        # Get all post variables
        title = request.POST['title']
        topic = request.POST['topic']
        related_area         = request.POST['related_area']
        description = request.POST['description']
        article = request.POST['article']
        photo = request.FILES['main_photo']
        


        # Create article
        article = Article(writer=user, title=title, topic=topic,
                          description=description, article=article,main_photo=photo)
        article.save()

        return redirect('accounts:dashboard', request.user.id)

    else:
        return redirect('accounts:dashboard',request.user.id)


def like(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            article_id = request.POST['article_id']
            article = Article.objects.get(id=article_id)
            if not Likes.objects.filter(liker_user=request.user, liked_article=article).exists():
                like = Likes(liker_user = request.user,liked_article = article)
                like.save()

                # We need to automatize this
                article.like_count +=1
                article.save()
                context = {
                "like_count":article.like_count,
                }
                return JsonResponse(context)
        else:
            return redirect("accounts:login")
    else:
        return redirect('articles:index')


def unlike(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            article_id = request.POST['article_id']
            article = Article.objects.get(id=article_id)
            like = Likes.objects.get(liker_user = request.user, liked_article=article)
            like.delete()

            # We need to automatize this
            article.like_count -=1
            article.save()
            context = {
                "like_count":article.like_count,
            }
    return JsonResponse(context)


def search(request):
    if request.method == "POST":
        text = request.POST["search"]
        articles = Article.objects.filter(title__contains=text)

        context = {
            'articles':articles
        }
    


    return render(request,'articles/articles.html',context)