# Generated by Django 2.2.5 on 2019-09-22 09:58

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_auto_20190922_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_photo',
            field=models.ImageField(blank=True, default='defaults/backround.jpg', upload_to=articles.models.upload_to),
        ),
    ]
