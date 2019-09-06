from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    birth_date          = models.DateField(null=True, blank=True)
    blogname		    = models.CharField(max_length=30,null=True, blank=True)
    description         = models.TextField(null=True, blank=True)
    about               = models.TextField(null=True, blank=True)
    articles            = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    follower            = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    followed            = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    liked_articles      = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    disliked_articles   = ArrayField(models.IntegerField(null=True, blank=True),null=True,blank=True)
    photo               = models.ImageField(upload_to='profile_photos/%Y/%m/%d/',null=True, blank=True)

    def __str__(self):
        return self.email