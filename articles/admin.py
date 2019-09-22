from django.contrib import admin
from .models import Article, Likes, Comments    
# Register your models here.

admin.site.register(Article)
admin.site.register(Likes)
admin.site.register(Comments)