from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from accounts.models import CustomUser

# Create your models here.

def upload_to(instance, filename):
    return 'images/%s/%s' % (instance.user.user.username, filename)

class Article(models.Model):
    writer          = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    article         = models.TextField(blank = True)
    title           = models.CharField(max_length=100)
    topic           = models.CharField(max_length=200)
    description     = models.TextField(blank = True)
    publish_date    = models.DateField(default=datetime.now)
    like_count      = models.IntegerField(default=0)
    dislike_count   = models.IntegerField(default=0)
    who_liked       = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    who_disliked    = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    is_edited       = models.BooleanField(default=False)
    last_edited     = models.DateField(default=datetime.now)
    seen_count      = models.IntegerField(default=0)
    comment_count   = models.IntegerField(default=0)
    main_photo      = models.ImageField(upload_to=upload_to,blank=True)
    photo_1         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_7         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_8         = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    
    def __str__(self):
        return self.title