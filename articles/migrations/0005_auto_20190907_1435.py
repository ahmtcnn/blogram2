# Generated by Django 2.2.4 on 2019-09-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190907_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dislike_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]