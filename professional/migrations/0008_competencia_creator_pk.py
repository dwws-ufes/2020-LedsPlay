# Generated by Django 3.2 on 2021-04-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0007_rename_competencia_profissional_competencias'),
    ]

    operations = [
        migrations.AddField(
            model_name='competencia',
            name='creator_pk',
            field=models.BigIntegerField(default=-1),
        ),
    ]
