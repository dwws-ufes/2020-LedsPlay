# Generated by Django 3.1.7 on 2021-04-01 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20210401_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='CEP',
            new_name='cidade',
        ),
    ]
