# Generated by Django 3.1.6 on 2021-02-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLogin', '0003_auto_20210215_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
