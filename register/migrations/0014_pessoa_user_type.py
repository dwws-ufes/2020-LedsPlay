# Generated by Django 3.1.7 on 2021-04-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20210401_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='user_type',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]