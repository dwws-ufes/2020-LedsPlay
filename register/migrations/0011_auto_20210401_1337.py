# Generated by Django 3.1.7 on 2021-04-01 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20210331_1959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordem',
            old_name='costumer',
            new_name='nome',
        ),
    ]
