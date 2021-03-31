# Generated by Django 3.1.7 on 2021-03-31 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210331_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='CEP',
            field=models.EmailField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nascimento',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
