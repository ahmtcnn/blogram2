# Generated by Django 2.2.4 on 2019-09-06 21:28

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_photo',
            field=models.ImageField(blank=True, upload_to=articles.models.upload_to),
        ),
    ]
