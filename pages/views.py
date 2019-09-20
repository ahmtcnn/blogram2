from django.shortcuts import render,redirect
from django.http import HttpResponse
from articles.models import Article,Likes

def index(request):
    if request.user.is_authenticated:
            # We fetch the article objects to print them on index page

        return redirect('articles:index')
    else:
        # We fetch the article objects to print them on index page
        articles = Article.objects.all()

        context = {
            'articles': articles,

            }

        return render(request, 'pages/index.html', context)


def about(request):
    return render(request,'pages/about.html')