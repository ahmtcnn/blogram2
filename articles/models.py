from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from accounts.models import CustomUser

# Create your models here.

area_choices = [
('sport', 'Sport'),
('social', 'Social'),
('science', 'Science'),
('cyber security', 'Cyber Security'),
('health', 'Health'),
('political', 'Political'),
('magazin', 'Magazin'),
]

def upload_to(instance, filename):
    return 'articles/%s/%s' % (instance.title, filename)


class Article(models.Model):
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article = models.TextField(blank=True)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    publish_date = models.DateField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    related_area = models.CharField(max_length=25, choices=area_choices,null=True)
    is_edited = models.BooleanField(default=False)
    last_edited = models.DateField(auto_now_add=True)
    seen_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    main_photo = models.ImageField(upload_to=upload_to, blank=True,default="defaults/backround.jpg")
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

class Likes(models.Model):
    liker_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="liker_user")
    liked_article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="liked_article")

    def __str__(self):
        return "%s -> %s" % (self.liker_user,self.liked_article)

    @staticmethod
    def get_liked_articles(CustomUser):
        liked_articles = Likes.objects.filter(liker_user=CustomUser)
        liked_articles_list  = []
        for likes in liked_articles:
            liked_articles_list.append(likes.liked_article)
        return liked_articles_list


class Comments(models.Model):
    article = models.ForeignKey("articles.Article", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.article.title