# Generated by Django 2.2.4 on 2019-09-07 11:35

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190906_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_to),
        ),
    ]
