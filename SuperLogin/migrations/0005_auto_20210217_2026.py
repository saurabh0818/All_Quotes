# Generated by Django 3.1.6 on 2021-02-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLogin', '0004_specialmessages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='author',
            name='lname',
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
