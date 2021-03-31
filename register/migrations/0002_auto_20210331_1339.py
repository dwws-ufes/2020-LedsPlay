# Generated by Django 3.1.7 on 2021-03-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=120),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='nome',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(max_length=1),
        ),
    ]
