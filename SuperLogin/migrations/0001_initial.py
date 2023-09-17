# Generated by Django 3.1.6 on 2021-02-15 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25, null=True)),
                ('lname', models.CharField(max_length=50, null=True)),
                ('occupation', models.CharField(max_length=20, null=True)),
                ('dob', models.DateField()),
                ('dod', models.DateField()),
                ('shortderc', models.CharField(max_length=100, null=True)),
                ('pic', models.ImageField(default='', upload_to='allquotes/images')),
                ('nationality', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotes', models.CharField(max_length=500, null=True)),
                ('type_quotes', models.CharField(max_length=50, null=True)),
                ('Author_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SuperLogin.author')),
            ],
        ),
    ]
