# Generated by Django 2.2.5 on 2019-09-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20190922_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='related_area',
            field=models.CharField(choices=[('sport', 'Sport'), ('political', 'Political'), ('health', 'Health'), ('magazin', 'Magazin'), ('cyber security', 'Cyber Security'), ('science', 'Science'), ('social', 'Social')], max_length=25, null=True),
        ),
    ]
