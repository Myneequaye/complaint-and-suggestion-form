# Generated by Django 3.0 on 2019-12-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='add_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
