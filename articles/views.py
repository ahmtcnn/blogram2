from django.shortcuts import render,redirect
from .models import Article
from accounts.models import CustomUser

# Create your views here.

def index(request):
    # We fetch the article objects to print them on index page
    articles = Article.objects.all()

    context = {
        'articles':articles,
    }

    return render(request, 'articles/articles.html',context)

def article(request, article_id):

    article = Article.objects.get(id=article_id)

    context = {

        'article':article,
    }

    return render(request, 'articles/article.html',context)

def search(request):
    return render(request, 'articles/search.html')


def save_article(request):
    # Check if request is post
    if request.method == 'POST':
        # Check if user is authenticated
        if request.user.is_authenticated:
            user_id = request.user.id
        
        # Get all post variables
        title       = request.POST['title']
        topic       = request.POST['topic']
        description = request.POST['description']
        article     = request.POST['article']

        # Get user object with id
        user = CustomUser.objects.get(id=user_id)

        # Create article
        article = Article(writer=user,title=title,topic=topic,description=description,article=article)
        article.save()
        
        # At the same time, we need to add this article's id to our user articles (integer list).
        if user.articles:
            user.articles.append(article.id)
        else:
            user.articles = [article.id]
        user.save()

        return redirect('accounts:dashboard', request.user.id)


    else:
        return redirect('accounts:dashboard')
