# Generated by Django 3.1.7 on 2021-04-08 15:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="auth.user",
                    ),
                ),
                ("nome", models.CharField(max_length=120, null=True)),
                ("sexo", models.CharField(max_length=1, null=True)),
                ("cidade", models.CharField(max_length=120, null=True)),
                (
                    "nascimento",
                    models.DateField(default=datetime.date.today, null=True),
                ),
                ("user_type", models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
    ]
