# Generated by Django 3.1.6 on 2021-02-23 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLogin', '0006_auto_20210217_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='spcl_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagories', models.CharField(max_length=5000, null=True)),
                ('images', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='specialmessages',
            name='sub_type',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='specialmessages',
            name='quotes_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SuperLogin.spcl_type'),
        ),
    ]
