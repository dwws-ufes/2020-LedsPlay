# Generated by Django 3.1.7 on 2021-03-31 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20210331_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competencia',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
