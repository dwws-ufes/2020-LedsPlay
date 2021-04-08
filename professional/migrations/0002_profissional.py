# Generated by Django 3.1.7 on 2021-04-08 15:41

import cpf_field.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("professional", "0001_initial"),
        ("register", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profissional",
            fields=[
                (
                    "pessoa_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="register.pessoa",
                    ),
                ),
                (
                    "cpf",
                    cpf_field.models.CPFField(
                        max_length=14, null=True, verbose_name="cpf"
                    ),
                ),
                (
                    "contato",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region="BR"
                    ),
                ),
                ("media", models.FloatField(null=True)),
            ],
            bases=("register.pessoa",),
        ),
    ]
