from django import forms
from django.forms import ModelForm, Textarea
from .models import Article



class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = [
            'title',
            'related_area',
            'description',
            'topic',
            'article',
            'main_photo',

        ]
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 2}),
        }

