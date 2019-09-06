# Generated by Django 2.2.4 on 2019-09-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190907_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dislike_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='like_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='seen_count',
            field=models.IntegerField(default=0),
        ),
    ]
