# Generated by Django 2.2.5 on 2019-09-18 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190907_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='disliked_articles',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='followed',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='liked_articles',
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_user', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]