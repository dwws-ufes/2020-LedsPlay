# Generated by Django 3.2 on 2021-04-07 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0004_auto_20210407_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordem',
            name='nome',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]