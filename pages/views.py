from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article

def index(request):

    articles = Article.objects.all()

    context = {
        'articles':articles,
    }


    return render(request,'pages/index.html',context)


def about(request):
    return render(request,'pages/about.html')