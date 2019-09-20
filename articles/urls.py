from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>',views.article, name='article'),
    path('search',views.search, name='search'),
    path('save_article', views.save_article, name="save_article"),
    path('like', views.like, name="like"),
    path('unlike', views.unlike, name="unlike"),

]
