from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


def upload_to(instance, filename):
    return 'profile_photos/%s/%s' % (instance.username, filename)


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    blogname = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to=upload_to, null=True, blank=True,default="defaults/avatar.png")

    def __str__(self):
        return self.email


class Follows(models.Model):
    follower = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="follower_user")
    followed = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="followed_user")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s -> %s" % (self.follower, self.followed)

    @staticmethod
    def get_followers(CustomUser):
        follows = Follows.objects.filter(followed=CustomUser)
        followers = []
        for follow in follows:
            followers.append(follow.follower)
        return followers

    @staticmethod
    def get_followed(CustomUser):
        follows = Follows.objects.filter(follower=CustomUser)
        followed = []
        for follow in follows:
            followed.append(follow.followed)

        return followed
