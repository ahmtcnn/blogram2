# Generated by Django 2.2.5 on 2019-09-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='related_area',
            field=models.CharField(choices=[('ME', '1'), ('YOU', '2'), ('WE', '3')], max_length=5, null=True),
        ),
    ]